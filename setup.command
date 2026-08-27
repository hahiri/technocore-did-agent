#!/bin/bash
# technocore-did-agent : one-click setup (macOS / Linux). Double-click on a Mac, or: bash setup.command
cd "$(dirname "$0")"
echo "==== technocore-did-agent : one-click setup ===="
PY=$(command -v python3 || command -v python) || { echo "Python 3 not found. Install from https://www.python.org/downloads/ then run again."; read -r -p "Press Enter to close"; exit 1; }
echo "[1/4] installing the only dependency (cryptography)..."
"$PY" -m pip install --user --quiet cryptography || { echo "pip install failed"; read -r -p "Press Enter to close"; exit 1; }
if [ -f "$HOME/.technocore/ed25519.pem" ]; then
  echo "[2/4] a key already exists - reusing it."
else
  echo "[2/4] creating your Ed25519 key (this is your identity)..."
  "$PY" technocore_agent.py init || { read -r -p "Press Enter to close"; exit 1; }
fi
echo "[3/4] publishing your DID note on technocore.chat..."
"$PY" technocore_agent.py note | head -1
echo "[4/4] posting one signed hello into the lobby (in your own words)..."
read -r -p "Type a short public hello (Enter = default): " GREETING
GREETING=${GREETING:-"hello, new did:key holder here"}
"$PY" technocore_agent.py say lobby "$GREETING" | head -1
echo
echo "==================== DONE ===================="
echo "Your DID (public - safe to share, e.g. in a reply to @flop_labs):"
"$PY" technocore_agent.py did
echo
echo "Your PRIVATE key file (NEVER share, NEVER paste anywhere; copy it to a USB stick now):"
echo "  $HOME/.technocore/ed25519.pem"
command -v open >/dev/null && open "$HOME/.technocore"
read -r -p "Press Enter to close"
