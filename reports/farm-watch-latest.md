# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-03 03:43Z / 対象: 2026-08-27 → 2026-09-03 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 37.4 (min 16.8 / max 50.6) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 20% (min 4% / max 64%)
- 履歴が流れるまでの推定時間: 平均 20 (min 11 / max 31) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 17682 → 54412 (+36730)
- 新規ルーム作成: 平均 390 (min 59 / max 828) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 104 (min 104 / max 104) / アクセプト 平均 46 (min 46 / max 46) / 参加 DID 平均 127 (min 127 / max 127)
- 累計フレーム seq: 3055

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 57% (min 51% / max 65%) (30 日平均の最新値 57%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 9 (min 3 / max 14) / マイナス銘柄数 平均 57 (min 45 / max 86)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $107M (min $21M / max $179M) / ショート清算 平均 $91M (min $27M / max $159M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-03 03:43Z / window 2026-08-27 → 2026-09-03 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 37.4 (min 16.8 / max 50.6) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 20% (min 4% / max 64%)
- estimated ring retention: mean 20 (min 11 / max 31) min

## Rooms
- listed room count: 17682 → 54412 (+36730)
- new rooms created: mean 390 (min 59 / max 828) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 104 (min 104 / max 104) / accepts mean 46 (min 46 / max 46) / distinct DIDs mean 127 (min 127 / max 127)
- cumulative frame seq: 3055

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 57% (min 51% / max 65%) (latest 30-day average 57%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 9 (min 3 / max 14) / negative symbols mean 57 (min 45 / max 86)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $107M (min $21M / max $179M) / short-liq mean $91M (min $27M / max $159M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
