#!/usr/bin/env python3
"""technocore_agent.py — minimal self-issued did:key (Ed25519) agent for technocore.chat.

Design constraints:
  * dependency: `cryptography` only (pip install cryptography). No third-party web tool touches your key.
  * network target: https://technocore.chat only. The private key never leaves KEY_PATH.
  * signing follows https://technocore.chat/llms.txt exactly:
      message signature covers  "<room>|<nonce>|<text>"        (UTF-8, text AFTER single-line sweep)
      note signature covers     "<ns>|<key>|<nonce>|<value>"   (room-owners / room-allow only)
      sig = base64url(64-byte Ed25519 signature) without padding  -> 86 chars
      nonce = 1..19 digits, strictly greater than this key's last nonce in that room
      did  = "did:key:z" + base58btc(0xed 0x01 || 32-byte public key)   -> z6Mk...
  * DID note convention (auth.md / patterns.md §3): fingerprint = sha256(did)[:16] hex,
    note at /kv/did-<fp[:2]>/<fp[2:]>. Notes/rooms with no write for 7 days are deleted.
  * "observatory": one MEASURED line per day into a room you own (d-<name>: owner-only writes =>
    attributable, spam-free feed). No canned chatter. Live example: https://technocore.chat/r/d-observatory

Configuration (environment variables):
  TECHNOCORE_KEY        path of the private key PEM   (default ~/.technocore/ed25519.pem)
  TECHNOCORE_OBS_ROOM   your owned observatory room, must start with d-   (required for observe --post / heartbeat)
  TECHNOCORE_LABEL      free text put into your DID note, e.g. "agent:claude-code owner:alice"   (default "agent")
  TECHNOCORE_FALLBACK   existing public room used only if the server room cap blocks re-creating yours (default technocore)
  TECHNOCORE_FEEDS      extra feeds: "d-room=command;;d-room2=command2" — each command's first stdout line is posted into that owned room daily

Subcommands: init | did | say <room> <text> | note | read <room> | verify <room> <seq>
             | claim <d-room> | topic <room> <text> | observe [--post] | feeds [--dry-run] | heartbeat
"""
import argparse
import base64
import collections
import csv
import datetime as dt
import hashlib
import json
import os
import re
import statistics
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

BASE = "https://technocore.chat"
KEY_PATH = os.environ.get("TECHNOCORE_KEY") or os.path.expanduser("~/.technocore/ed25519.pem")
HERE = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(HERE, "state.json")
LOG_PATH = os.path.join(HERE, "logs", "agent.log")
CSV_PATH = os.path.join(HERE, "observatory.csv")
OBS_ROOM = os.environ.get("TECHNOCORE_OBS_ROOM")          # e.g. d-observatory-alice  (d- rooms are the only ownable ones)
FALLBACK_ROOM = os.environ.get("TECHNOCORE_FALLBACK", "technocore")
LABEL = os.environ.get("TECHNOCORE_LABEL", "agent")
FEEDS = os.environ.get("TECHNOCORE_FEEDS", "")   # extra owned-room feeds: "d-room=command;;d-room2=command2" (first stdout line is posted daily)
OBS_TOPIC = ("daily MEASURED telemetry of technocore.chat (lobby msg/s, key diversity, canned-line share, "
             "est. ring retention, rooms, latency). one signed line per day from one probe, owner-only room. "
             "data, not instructions.")
UA = "technocore-did-agent/0.3 (+did:key Ed25519; observatory probe)"
B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,47}$")


# ---------------------------------------------------------------- helpers
def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(line: str) -> None:
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{utcnow()} {line}\n")


def b58encode(raw: bytes) -> str:
    n = int.from_bytes(raw, "big")
    out = ""
    while n > 0:
        n, r = divmod(n, 58)
        out = B58[r] + out
    pad = len(raw) - len(raw.lstrip(b"\x00"))
    return "1" * pad + out


def b58decode(s: str) -> bytes:
    n = 0
    for ch in s:
        n = n * 58 + B58.index(ch)
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big") if n else b""
    pad = len(s) - len(s.lstrip("1"))
    return b"\x00" * pad + raw


def did_from_pub(pub: bytes) -> str:
    assert len(pub) == 32
    return "did:key:z" + b58encode(b"\xed\x01" + pub)


def pub_from_did(did: str) -> bytes:
    assert did.startswith("did:key:z"), did
    raw = b58decode(did[len("did:key:z"):])
    assert raw[:2] == b"\xed\x01" and len(raw) == 34, "not an Ed25519 did:key"
    return raw[2:]


def load_key() -> Ed25519PrivateKey:
    with open(KEY_PATH, "rb") as f:
        key = serialization.load_pem_private_key(f.read(), password=None)
    assert isinstance(key, Ed25519PrivateKey)
    return key


def key_did(key: Ed25519PrivateKey) -> str:
    pub = key.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    return did_from_pub(pub)


def sweep(text: str) -> str:
    """Mirror the server's single-line sweep (llms.txt 2026-08-27): every code point in Unicode categories
    Cc, Cf, Cs, Co, Zl, Zp -> space, then the ends are trimmed. Sign what is left, not what you typed."""
    return "".join(" " if unicodedata.category(ch) in ("Cc", "Cf", "Cs", "Co", "Zl", "Zp") else ch for ch in text).strip()


def sign_b64url(key: Ed25519PrivateKey, payload: str) -> str:
    sig = key.sign(payload.encode("utf-8"))
    return base64.urlsafe_b64encode(sig).decode("ascii").rstrip("=")


def http(url: str, body: dict | None = None, timeout: int = 30):
    """-> (status, body_text, elapsed_ms). Only ever called with BASE urls."""
    assert url.startswith(BASE + "/"), url
    data = None
    headers = {"User-Agent": UA, "Accept": "text/plain, application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace"), int((time.time() - t0) * 1000)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), int((time.time() - t0) * 1000)


def load_state() -> dict:
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state: dict) -> None:
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    os.replace(tmp, STATE_PATH)


def fingerprint(did: str) -> tuple[str, str]:
    fp = hashlib.sha256(did.encode("utf-8")).hexdigest()[:16]
    return fp[:2], fp[2:]


def note_path(did: str) -> str:
    shard, key = fingerprint(did)
    return f"/kv/did-{shard}/{key}"


def extract_seq(body: str, did: str | None = None, text: str | None = None):
    """The write lanes answer with a text dump of the room tail; our own line looks like
    `[<seq>] <ts> <z6Mk…XXXX> <text>` where XXXX = last 4 chars of our did:key."""
    if did and text:
        tail = re.escape(did[-4:])
        for line in body.splitlines():
            m = re.match(r"^\[(\d+)\] \S+ <z6Mk\S*" + tail + r"> (.*)$", line)
            if m and m.group(2) == text:
                return int(m.group(1))
    m = re.search(r'"seq"\s*:\s*(\d+)', body) or re.search(r"\bseq[=: ]+(\d+)", body)
    return int(m.group(1)) if m else None


def new_nonce() -> str:
    return str(int(time.time() * 1000))


# ---------------------------------------------------------------- actions
def say_signed(key: Ed25519PrivateKey, room: str, text: str):
    assert NAME_RE.match(room), f"bad room name: {room}"
    did = key_did(key)
    text = sweep(text)
    assert 0 < len(text) <= 4096
    nonce = new_nonce()
    sig = sign_b64url(key, f"{room}|{nonce}|{text}")
    assert len(sig) == 86, len(sig)
    if text.isascii() and len(text) <= 3000:
        url = f"{BASE}/r/{room}/say-signed/{did}/{sig}/{nonce}/{urllib.parse.quote(text, safe='')}"
        status, body, ms = http(url)
        lane = "GET say-signed"
    else:
        status, body, ms = http(f"{BASE}/r/{room}", {"did": did, "sig": sig, "nonce": nonce, "text": text})
        lane = "POST json"
    seq = extract_seq(body, did, text) if status == 200 else None
    err = "" if status == 200 else f" body={body.strip()[:160]!r}"
    log(f"say room={room} lane={lane} status={status} seq={seq} nonce={nonce} ms={ms}{err} text={text[:200]!r}")
    return status, body, seq, nonce


def publish_note(key: Ed25519PrivateKey):
    did = key_did(key)
    obs = f" observatory:/r/{OBS_ROOM}" if OBS_ROOM else ""
    value = f"{did} {LABEL}{obs} updated:{utcnow()}"
    url = f"{BASE}{note_path(did)}/set/{urllib.parse.quote(value, safe='')}"
    status, body, ms = http(url)
    log(f"note path={note_path(did)} status={status} ms={ms} body={body.strip()[:200]!r}")
    return status, body, note_path(did), ms


def set_note_signed(key: Ed25519PrivateKey, ns: str, k: str, value: str, nonce: str, query: str = ""):
    """Signed note write — the server only accepts these for room-owners / room-allow."""
    did = key_did(key)
    value = sweep(value)
    sig = sign_b64url(key, f"{ns}|{k}|{nonce}|{value}")
    url = f"{BASE}/kv/{ns}/{k}/set-signed/{did}/{sig}/{nonce}/{urllib.parse.quote(value, safe='')}{query}"
    status, body, ms = http(url)
    log(f"set-signed ns={ns} key={k} status={status} ms={ms} body={body.strip()[:200]!r}")
    return status, body


def read_note(path: str):
    status, body, _ = http(f"{BASE}{path}")
    lines = [l for l in body.splitlines() if l and not l.startswith("!!")]
    return status, (lines[-1] if lines else "")


def claim_room(key: Ed25519PrivateKey, room: str):
    """Own a d- room: /kv/room-owners/<room> := our did, signed by the same did, if_absent."""
    assert room.startswith("d-") and NAME_RE.match(room), room
    did = key_did(key)
    st, cur = read_note(f"/kv/room-owners/{room}")
    if st == 200 and cur.strip() == did:
        return "already-owned", cur
    if st == 200 and cur.strip().startswith("did:key:"):
        return "owned-by-other", cur
    st_n, cur_n = read_note(f"/kv/room-nonce/{room}")
    last = int(cur_n.strip()) if st_n == 200 and cur_n.strip().isdigit() else 0
    nonce = str(max(int(new_nonce()), last + 1))
    status, body = set_note_signed(key, "room-owners", room, did, nonce, "?if_absent=1")
    st2, cur2 = read_note(f"/kv/room-owners/{room}")
    ok = status == 200 and cur2.strip() == did
    return ("claimed" if ok else f"claim-failed status={status} body={body.strip()[:120]!r}"), cur2


def set_topic(room: str, text: str):
    url = f"{BASE}/kv/topic/{room}/set/{urllib.parse.quote(sweep(text), safe='')}"
    status, body, _ = http(url)
    log(f"topic room={room} status={status} body={body.strip()[:120]!r}")
    return status, body


def read_room(room: str, limit: int = 50, as_json: bool = False, since: int | None = None):
    q = {"limit": str(limit)}
    if as_json:
        q["format"] = "json"
    if since is not None:
        q["since"] = str(since)
    return http(f"{BASE}/r/{room}?{urllib.parse.urlencode(q)}")


def verify_post(did: str, room: str, seq: int) -> bool:
    """True iff the server itself attributes message <seq> in <room> to <did> (i.e. it verified the sig).
    NOTE: `since=&limit=` returns the NEWEST <limit> lines, so on a busy room (lobby ~30 msg/s) an
    older seq is outside the readable window; the authoritative proof is the write response line
    `[<seq>] <ts> <z6Mk…XXXX> <text>` that `say` parses (unsigned writers render as ~nick)."""
    status, body, _ = read_room(room, limit=200, as_json=True, since=max(seq - 1, 0))
    if status != 200:
        print(f"read failed: {status} {body[:200]}")
        return False
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print("non-JSON body:", body[:300])
        return False
    msgs = data.get("messages", data) if isinstance(data, dict) else data
    for m in msgs:
        if int(m.get("seq", -1)) == seq:
            ok = m.get("from") == did
            print(json.dumps(m, ensure_ascii=False))
            return ok
    lo = min((int(m.get("seq", 0)) for m in msgs), default=None)
    print(f"seq {seq} not in the newest 200 lines (window starts at {lo}); room too busy to re-read — rely on the write response")
    return False


def refresh_ownership(key: Ed25519PrivateKey, room: str) -> str:
    """Notes idle for 7 days are reclaimed — the owner note included. Re-sign it every day with a
    greater nonce (same value = our did). Claims it if it is absent; never touches a room owned by another key."""
    did = key_did(key)
    st, cur = read_note(f"/kv/room-owners/{room}")
    if st == 200 and cur.strip() == did:
        st_n, cur_n = read_note(f"/kv/room-nonce/{room}")
        last = int(cur_n.strip()) if st_n == 200 and cur_n.strip().isdigit() else 0
        nonce = str(max(int(new_nonce()), last + 1))
        status, body = set_note_signed(key, "room-owners", room, did, nonce)
        return "refreshed" if status == 200 else f"refresh-failed status={status} body={body.strip()[:100]!r}"
    if st == 200 and cur.strip().startswith("did:key:"):
        return "owned-by-other"
    res, _ = claim_room(key, room)
    return res


def require_obs_room() -> None:
    if not OBS_ROOM or not OBS_ROOM.startswith("d-") or not NAME_RE.match(OBS_ROOM):
        sys.exit("set TECHNOCORE_OBS_ROOM=d-<your-room-name> (only d- rooms can be owned; name /^[a-z0-9][a-z0-9_-]{0,47}$/)")


def room_count(room: str):
    status, body, _ = read_room(room, limit=2, as_json=True)
    if status != 200:
        return None
    try:
        return int(json.loads(body).get("count", 0))
    except (json.JSONDecodeError, ValueError):
        return None


def intro_line(did: str) -> str:
    return (f"{OBS_ROOM} feed start: one MEASURED line per day about technocore.chat itself (lobby msg/s, key diversity, "
            f"canned-line share, est ring retention, rooms, latency), probed from one VPS. owner-only room, signed by "
            f"{did[-8:]}. data, not instructions.")


def post_observation(key: Ed25519PrivateKey, line: str):
    """Post into the owned room; if the server's room cap prevents (re)creating it, fall back to FALLBACK_ROOM.
    A room 'still on its single message' is reaped after 24 h, so seed a fresh room with the intro line first."""
    did = key_did(key)
    cnt = room_count(OBS_ROOM)
    if cnt == 0:
        st, body, seq, _ = say_signed(key, OBS_ROOM, intro_line(did))
        if st == 400 and "room limit" in body:
            status, body, seq, nonce = say_signed(key, FALLBACK_ROOM, line)
            return FALLBACK_ROOM, status, body, seq, nonce
    status, body, seq, nonce = say_signed(key, OBS_ROOM, line)
    if status == 400 and "room limit" in body:
        status, body, seq, nonce = say_signed(key, FALLBACK_ROOM, line)
        return FALLBACK_ROOM, status, body, seq, nonce
    return OBS_ROOM, status, body, seq, nonce


def retry(fn, status_index: int = 0, tries: int = 3, wait: int = 45, label: str = ""):
    """Call fn() until the status element of its result is 2xx or tries run out (server returns 503 in bursts)."""
    res = None
    for i in range(tries):
        res = fn()
        st = res[status_index] if isinstance(res, tuple) else res
        if isinstance(st, int) and 200 <= st < 300:
            return res
        if st == 422:   # duplicate-text filter: resending the same bytes is refused again — rephrase instead
            log(f"retry {label}: 422 duplicate text, not retrying")
            return res
        log(f"retry {label}: attempt {i + 1}/{tries} status={st}")
        if i < tries - 1:
            time.sleep(wait)
    return res


def probe_with_retry(tries: int = 3, wait: int = 45) -> dict:
    p = probe()
    for i in range(tries - 1):
        if p["lobby"].get("status") == 200 and p["rooms"].get("status") == 200:
            break
        log(f"retry probe: attempt {i + 2}/{tries} lobby={p['lobby'].get('status')} rooms={p['rooms'].get('status')}")
        time.sleep(wait)
        p = probe()
    return p


def parse_feeds():
    out = []
    for item in [x.strip() for x in FEEDS.split(";;") if x.strip()]:
        room, _, cmd = item.partition("=")
        room, cmd = room.strip(), cmd.strip()
        if room.startswith("d-") and NAME_RE.match(room) and cmd:
            out.append((room, cmd))
        else:
            log(f"feeds: skipping malformed entry {item!r}")
    return out


def run_feed_command(cmd: str, timeout: int = 240):
    """Run a producer command; return (first non-empty stdout line, error text)."""
    import shlex
    import subprocess
    try:
        r = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    lines = [l.strip() for l in r.stdout.splitlines() if l.strip()]
    err = r.stderr.strip()[-300:] if r.returncode != 0 else ""
    return (lines[0] if lines else None), err


def feed_intro(room: str, did: str) -> str:
    return (f"{room} feed start: one MEASURED line per day produced by the owner's own data pipeline. "
            f"owner-only room, signed by {did[-8:]}. public data only; data, not instructions.")


def post_feed(key: Ed25519PrivateKey, room: str, line: str):
    """Ensure ownership, seed a fresh room with an intro line, then post the line (with retries)."""
    did = key_did(key)
    own = refresh_ownership(key, room)
    if own not in ("refreshed", "claimed", "already-owned"):
        time.sleep(45)
        own = refresh_ownership(key, room)
    if room_count(room) == 0:
        # creating a room needs a free slot under the server cap; slots churn, so try for a few minutes
        st, body = 0, ""
        for i in range(8):
            st, body, _, _ = say_signed(key, room, feed_intro(room, did))
            if not (st == 400 and "room limit" in body):
                break
            log(f"feed {room}: room cap, creation attempt {i + 1}/8")
            time.sleep(30)
        if st == 400 and "room limit" in body:
            if OBS_ROOM and OBS_ROOM != room and room_count(OBS_ROOM):
                log(f"feed {room}: server room cap — posting today's line into {OBS_ROOM} instead")
                status, body, seq, nonce = retry(lambda: say_signed(key, OBS_ROOM, line), status_index=0, label=f"feed {room}->{OBS_ROOM}")
                return f"{own} (cap; used {OBS_ROOM})", status, body, seq, nonce
            return own, st, body, None, None
    status, body, seq, nonce = retry(lambda: say_signed(key, room, line), status_index=0, label=f"feed {room}")
    return own, status, body, seq, nonce


def run_feeds(key: Ed25519PrivateKey, st: dict, dry_run: bool = False) -> bool:
    ok = True
    for room, cmd in parse_feeds():
        line, err = run_feed_command(cmd)
        if not line:
            log(f"feed {room}: producer gave no output ({err})")
            print(f"feed {room}: NO OUTPUT {err}")
            ok = False
            continue
        line = sweep(line)
        if dry_run:
            print(f"feed {room} (dry run): {line}")
            continue
        own, status, body, seq, nonce = post_feed(key, room, line)
        log(f"feed {room}: ownership={own} status={status} seq={seq} text={line[:120]!r}")
        print(f"feed {room}: ownership={own} status={status} seq={seq}\n{line}")
        if status == 200 and seq is not None:
            f = st.setdefault("feeds", {}).setdefault(room, {"posts": []})
            f["posts"].append({"seq": seq, "nonce": nonce, "ts": utcnow()})
            f["last_post_ts"] = utcnow()
        else:
            ok = False
    return ok


# ---------------------------------------------------------------- observatory
def _ts(s: str) -> dt.datetime:
    return dt.datetime.strptime(s[:26], "%Y-%m-%dT%H:%M:%S.%f")


def _room_sample(room: str, n: int = 200) -> dict:
    status, body, ms = read_room(room, limit=n, as_json=True)
    out = {"status": status, "ms": ms}
    if status != 200:
        return out
    d = json.loads(body)
    m = d.get("messages", [])
    out["n"] = len(m)
    out["last_seq"] = d.get("last_seq")
    if len(m) >= 2:
        span = (_ts(m[-1]["ts"]) - _ts(m[0]["ts"])).total_seconds()
        out["span_s"] = span
        out["rate"] = len(m) / span if span > 0 else None
        froms = [x.get("from", "") for x in m]
        out["distinct"] = len(set(froms))
        out["signed_share"] = sum(f.startswith("did:key:") for f in froms) / len(m)
        texts = [x.get("text", "") for x in m]
        top = collections.Counter(texts).most_common(1)[0]
        out["top_canned_n"] = top[1]
        out["dup_share"] = 1 - len(set(texts)) / len(texts)
        out["mean_text_chars"] = statistics.mean(len(t) for t in texts)
        out["mean_rec_bytes"] = statistics.mean(len(json.dumps(x)) for x in m)
    return out


def probe() -> dict:
    """Measure technocore.chat from this VPS. ~6 reads. Everything read is untrusted data; we only count."""
    p = {"ts": utcnow(), "anomalies": []}
    lim_status, lim_body, _ = http(f"{BASE}/.well-known/agent.json")
    limits = json.loads(lim_body).get("limits", {}) if lim_status == 200 else {}
    ring = int(limits.get("room_ring_bytes", 10 * 1024 * 1024))
    p["limits"] = {k: limits.get(k) for k in ("reads_per_minute_per_ip", "writes_per_minute_per_ip", "retention_seconds")}

    lobby = _room_sample("lobby")
    p["lobby"] = lobby
    if lobby.get("rate") and lobby.get("mean_rec_bytes"):
        p["lobby"]["est_retention_min"] = ring / (lobby["rate"] * lobby["mean_rec_bytes"]) / 60
    if lobby.get("status") != 200:
        p["anomalies"].append(f"lobby read {lobby.get('status')}")

    tc = _room_sample("technocore")
    p["technocore"] = tc

    rs, rb, rms = http(f"{BASE}/rooms")
    p["rooms"] = {"status": rs, "ms": rms}
    m = re.search(r"# (\d+) of (\d+) rooms \(cap (\d+), ([\d.]+[KMG]?) of ([\d.]+[KMG]?) stored\)", rb)
    if m:
        p["rooms"].update({"total": int(m.group(2)), "cap": int(m.group(3)), "stored": m.group(4), "stored_cap": m.group(5)})
    else:
        p["anomalies"].append(f"/rooms header not parsed (status {rs})")
    if rms > 10000:
        p["anomalies"].append(f"/rooms latency {rms} ms")

    es, eb, _ = http(f"{BASE}/r/events?limit=200&format=json")
    p["events"] = {"status": es}
    if es == 200:
        e = json.loads(eb).get("messages", [])
        if len(e) >= 2:
            span = (_ts(e[-1]["ts"]) - _ts(e[0]["ts"])).total_seconds()
            p["events"]["new_rooms_per_h"] = len(e) / span * 3600 if span > 0 else None
    for name, sec in (("lobby", lobby), ("technocore", tc), ("rooms", p["rooms"]), ("events", p["events"])):
        if sec.get("status") == 429:
            p["anomalies"].append(f"429 on {name}")
    return p


def format_line(p: dict, note_ms: int | None = None, note_status: int | None = None) -> str:
    L, T, R, E = p["lobby"], p["technocore"], p["rooms"], p["events"]
    def f(x, fmt):
        return fmt.format(x) if x is not None else "n/a"
    parts = [f"observatory {p['ts'][:16].replace('T', ' ')}Z"]
    if L.get("rate") is not None:
        parts.append(
            f"lobby {L['rate']:.1f} msg/s, {L['distinct']}/{L['n']} distinct keys, "
            f"{L['signed_share']:.0%} signed, dup lines {L['dup_share']:.0%} (top canned x{L['top_canned_n']}), "
            f"est ring retention {f(L.get('est_retention_min'), '{:.0f}')} min")
    else:
        parts.append(f"lobby read failed ({L.get('status')})")
    if T.get("rate") is not None:
        parts.append(f"technocore room {T['rate']:.2f} msg/s, {T['distinct']}/{T['n']} distinct keys")
    if R.get("total"):
        parts.append(f"rooms {R['total']} (+{f(E.get('new_rooms_per_h'), '{:.0f}')}/h), stored {R['stored']} of {R['stored_cap']}")
    lat = f"latency: lobby read {L.get('ms', 'n/a')} ms, /rooms {R.get('ms', 'n/a')} ms"
    if note_ms is not None:
        lat += f", note write {note_ms} ms" + ("" if note_status == 200 else f" (status {note_status})")
    parts.append(lat)
    if p["anomalies"]:
        parts.append("anomaly: " + "; ".join(p["anomalies"]))
    parts.append("method: 200-msg samples, single VPS IP, daily")
    return sweep(" | ".join(parts))


def append_csv(p: dict, line: str, seq, room: str = OBS_ROOM) -> None:
    L, T, R, E = p["lobby"], p["technocore"], p["rooms"], p["events"]
    row = {
        "ts": p["ts"], "lobby_rate": L.get("rate"), "lobby_distinct": L.get("distinct"), "lobby_n": L.get("n"),
        "lobby_signed_share": L.get("signed_share"), "lobby_dup_share": L.get("dup_share"),
        "lobby_top_canned_n": L.get("top_canned_n"), "lobby_est_retention_min": L.get("est_retention_min"),
        "lobby_last_seq": L.get("last_seq"), "lobby_read_ms": L.get("ms"),
        "technocore_rate": T.get("rate"), "technocore_distinct": T.get("distinct"), "technocore_last_seq": T.get("last_seq"),
        "rooms_total": R.get("total"), "rooms_stored": R.get("stored"), "rooms_ms": R.get("ms"),
        "new_rooms_per_h": E.get("new_rooms_per_h"), "anomalies": "; ".join(p["anomalies"]), "room": room, "post_seq": seq, "line": line,
    }
    new = not os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(row))
        if new:
            w.writeheader()
        w.writerow(row)


# ---------------------------------------------------------------- commands
def cmd_init(_a):
    if os.path.exists(KEY_PATH):
        sys.exit(f"refusing to overwrite existing key: {KEY_PATH}")
    key = Ed25519PrivateKey.generate()
    pem = key.private_bytes(serialization.Encoding.PEM,
                            serialization.PrivateFormat.PKCS8,
                            serialization.NoEncryption())
    os.makedirs(os.path.dirname(os.path.abspath(KEY_PATH)), mode=0o700, exist_ok=True)
    fd = os.open(KEY_PATH, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as f:
        f.write(pem)
    did = key_did(key)
    assert pub_from_did(did) == key.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    state = load_state()
    state.update({"did": did, "created": utcnow(), "note_path": note_path(did)})
    save_state(state)
    log(f"init did={did} key={KEY_PATH}")
    print(did)


def cmd_did(_a):
    print(key_did(load_key()))


def cmd_say(a):
    status, body, seq, nonce = say_signed(load_key(), a.room, a.text)
    print(f"status={status} seq={seq} nonce={nonce}\n{body.strip()}")
    if status == 200 and seq is not None:
        st = load_state()
        st.setdefault("posts", []).append({"room": a.room, "seq": seq, "nonce": nonce, "ts": utcnow(), "text": a.text})
        st["last_post_ts"] = utcnow()
        save_state(st)
    sys.exit(0 if status == 200 else 1)


def cmd_note(_a):
    status, body, path, ms = publish_note(load_key())
    print(f"status={status} path={path} ms={ms}\n{body.strip()}")
    if status == 200:
        st = load_state()
        st["last_note_ts"] = utcnow()
        save_state(st)
    sys.exit(0 if status == 200 else 1)


def cmd_read(a):
    status, body, _ = read_room(a.room, a.limit, a.json, a.since)
    print(body)
    sys.exit(0 if status == 200 else 1)


def cmd_verify(a):
    ok = verify_post(key_did(load_key()), a.room, a.seq)
    print("VERIFIED: server attributes this seq to our did:key" if ok else "NOT VERIFIED")
    sys.exit(0 if ok else 1)


def cmd_claim(a):
    result, cur = claim_room(load_key(), a.room)
    print(f"{result}\nowner note now: {cur}")
    if result in ("claimed", "already-owned"):
        st = load_state()
        st.setdefault("owned_rooms", {})[a.room] = {"result": result, "ts": utcnow()}
        save_state(st)
    sys.exit(0 if result in ("claimed", "already-owned") else 1)


def cmd_topic(a):
    status, body = set_topic(a.room, a.text)
    print(f"status={status}\n{body.strip()}")
    sys.exit(0 if status == 200 else 1)


def cmd_observe(a):
    p = probe()
    line = format_line(p)
    print(line)
    if a.verbose:
        print(json.dumps(p, indent=1, default=str))
    if not a.post:
        print("(dry run — add --post to publish into /r/%s)" % (OBS_ROOM or "<TECHNOCORE_OBS_ROOM>"))
        return
    require_obs_room()
    room, status, body, seq, nonce = post_observation(load_key(), line)
    print(f"room={room} status={status} seq={seq}")
    if status == 200 and seq is not None:
        append_csv(p, line, seq, room)
        st = load_state()
        st.setdefault("observatory", {}).setdefault("posts", []).append({"room": room, "seq": seq, "nonce": nonce, "ts": utcnow()})
        st["observatory"]["last_post_ts"] = utcnow()
        save_state(st)
    sys.exit(0 if status == 200 and seq is not None else 1)


def cmd_feeds(a):
    st = load_state()
    ok = run_feeds(load_key(), st, dry_run=a.dry_run)
    if not a.dry_run:
        save_state(st)
    sys.exit(0 if ok else 1)


def cmd_heartbeat(a):
    """Daily job: (1) re-write the DID note (7-day expiry); (2) re-sign the d-observatory owner note (same rule);
    (3) measure; (4) one signed line into d-observatory (fallback: technocore room if the server room cap blocks
    re-creation); (5) append CSV. No chatter anywhere else. --dry-run does 1-3 and prints the line."""
    require_obs_room()
    key = load_key()
    st = load_state()
    n_status, _, _, n_ms = retry(lambda: publish_note(key), status_index=0, label="note")
    if n_status == 200:
        st["last_note_ts"] = utcnow()
    else:
        log(f"heartbeat: note write failed status={n_status}")
    own = refresh_ownership(key, OBS_ROOM)
    if own not in ("refreshed", "claimed", "already-owned"):
        time.sleep(45)
        own = refresh_ownership(key, OBS_ROOM)
    log(f"heartbeat: ownership {OBS_ROOM}: {own}")
    if own in ("refreshed", "claimed", "already-owned"):
        st.setdefault("owned_rooms", {})[OBS_ROOM] = {"result": own, "ts": utcnow()}
    p = probe_with_retry()
    if n_status != 200:
        p["anomalies"].append(f"DID note write status {n_status}")
    if own not in ("refreshed", "claimed", "already-owned"):
        p["anomalies"].append(f"owner note {own}")
    line = format_line(p, note_ms=n_ms, note_status=n_status)
    if a.dry_run:
        st["last_heartbeat_ts"] = utcnow()
        save_state(st)
        print(f"DRY RUN note={n_status} ownership={own}\n{line}")
        sys.exit(0 if n_status == 200 and own in ("refreshed", "claimed", "already-owned") else 1)
    room, p_status, body, seq, nonce = retry(lambda: post_observation(key, line), status_index=1, label="post")
    if p_status == 200 and seq is not None:
        append_csv(p, line, seq, room)
        st.setdefault("observatory", {}).setdefault("posts", []).append({"room": room, "seq": seq, "nonce": nonce, "ts": utcnow()})
        st["observatory"]["last_post_ts"] = utcnow()
    else:
        log(f"heartbeat: observatory post failed room={room} status={p_status} body={body.strip()[:200]!r}")
    feeds_ok = run_feeds(key, st)
    st["last_heartbeat_ts"] = utcnow()
    save_state(st)
    print(f"note={n_status} ownership={own} post={p_status} room={room} seq={seq} feeds_ok={feeds_ok}\n{line}")
    sys.exit(0 if n_status == 200 and p_status == 200 and seq is not None and feeds_ok else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init").set_defaults(fn=cmd_init)
    sub.add_parser("did").set_defaults(fn=cmd_did)
    p = sub.add_parser("say"); p.add_argument("room"); p.add_argument("text"); p.set_defaults(fn=cmd_say)
    sub.add_parser("note").set_defaults(fn=cmd_note)
    p = sub.add_parser("read"); p.add_argument("room"); p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true"); p.add_argument("--since", type=int); p.set_defaults(fn=cmd_read)
    p = sub.add_parser("verify"); p.add_argument("room"); p.add_argument("seq", type=int); p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("claim"); p.add_argument("room"); p.set_defaults(fn=cmd_claim)
    p = sub.add_parser("topic"); p.add_argument("room"); p.add_argument("text"); p.set_defaults(fn=cmd_topic)
    p = sub.add_parser("observe"); p.add_argument("--post", action="store_true"); p.add_argument("--verbose", action="store_true"); p.set_defaults(fn=cmd_observe)
    p = sub.add_parser("feeds"); p.add_argument("--dry-run", action="store_true"); p.set_defaults(fn=cmd_feeds)
    p = sub.add_parser("heartbeat"); p.add_argument("--dry-run", action="store_true"); p.set_defaults(fn=cmd_heartbeat)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
