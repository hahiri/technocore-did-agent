# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-17 03:42Z / 対象: 2026-09-10 → 2026-09-17 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 24.8 (min 19.0 / max 35.4) msg/s
- 200 件中の別々の鍵の割合: 平均 97% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 27% (min 19% / max 43%)
- 履歴が流れるまでの推定時間: 平均 22 (min 14 / max 27) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 54848 → 92165 (+37317)
- 新規ルーム作成: 平均 1234 (min 106 / max 3544) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 27 (min 17 / max 50) / アクセプト 平均 152 (min 122 / max 176) / 参加 DID 平均 57 (min 37 / max 83)
- 累計フレーム seq: 2224158 → 5575023 (+3350865)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 62% (min 56% / max 71%) (30 日平均の最新値 55%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 7 (min 2 / max 13) / マイナス銘柄数 平均 86 (min 61 / max 110)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $144M (min $51M / max $295M) / ショート清算 平均 $106M (min $52M / max $192M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-17 03:42Z / window 2026-09-10 → 2026-09-17 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 24.8 (min 19.0 / max 35.4) msg/s
- distinct keys per 200 messages: mean 97% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 27% (min 19% / max 43%)
- estimated ring retention: mean 22 (min 14 / max 27) min

## Rooms
- listed room count: 54848 → 92165 (+37317)
- new rooms created: mean 1234 (min 106 / max 3544) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 27 (min 17 / max 50) / accepts mean 152 (min 122 / max 176) / distinct DIDs mean 57 (min 37 / max 83)
- cumulative frame seq: 2224158 → 5575023 (+3350865)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 62% (min 56% / max 71%) (latest 30-day average 55%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 7 (min 2 / max 13) / negative symbols mean 86 (min 61 / max 110)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $144M (min $51M / max $295M) / short-liq mean $106M (min $52M / max $192M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
