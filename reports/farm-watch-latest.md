# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-11-08 03:49Z / 対象: 2026-11-02 → 2026-11-08 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 22.6 (min 9.2 / max 42.2) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 8% (min 2% / max 22%)
- 履歴が流れるまでの推定時間: 平均 28 (min 12 / max 55) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 20181 → 53385 (+33204)
- 新規ルーム作成: 平均 1068 (min 90 / max 3415) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 33 (min 27 / max 38) / アクセプト 平均 137 (min 120 / max 150) / 参加 DID 平均 57 (min 30 / max 74)
- 累計フレーム seq: 25086790 → 25496313 (+409523)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 55% (min 51% / max 61%) (30 日平均の最新値 61%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 16 (min 7 / max 30) / マイナス銘柄数 平均 61 (min 42 / max 103)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $177M (min $27M / max $591M) / ショート清算 平均 $93M (min $14M / max $253M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-11-08 03:49Z / window 2026-11-02 → 2026-11-08 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 22.6 (min 9.2 / max 42.2) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 8% (min 2% / max 22%)
- estimated ring retention: mean 28 (min 12 / max 55) min

## Rooms
- listed room count: 20181 → 53385 (+33204)
- new rooms created: mean 1068 (min 90 / max 3415) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 33 (min 27 / max 38) / accepts mean 137 (min 120 / max 150) / distinct DIDs mean 57 (min 30 / max 74)
- cumulative frame seq: 25086790 → 25496313 (+409523)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 55% (min 51% / max 61%) (latest 30-day average 61%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 16 (min 7 / max 30) / negative symbols mean 61 (min 42 / max 103)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $177M (min $27M / max $591M) / short-liq mean $93M (min $14M / max $253M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
