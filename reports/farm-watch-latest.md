# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-10-11 03:40Z / 対象: 2026-10-04 → 2026-10-11 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 24.1 (min 13.4 / max 38.1) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 10% (min 2% / max 19%)
- 履歴が流れるまでの推定時間: 平均 24 (min 14 / max 38) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 20348 → 20348 (+0)
- 新規ルーム作成: 平均 856 (min 95 / max 3164) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 20 (min 14 / max 25) / アクセプト 平均 165 (min 160 / max 171) / 参加 DID 平均 40 (min 31 / max 54)
- 累計フレーム seq: 19517560 → 21951753 (+2434193)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 55% (min 47% / max 63%) (30 日平均の最新値 53%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 7 (min 1 / max 14) / マイナス銘柄数 平均 56 (min 30 / max 80)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $145M (min $19M / max $585M) / ショート清算 平均 $75M (min $20M / max $213M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-10-11 03:40Z / window 2026-10-04 → 2026-10-11 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 24.1 (min 13.4 / max 38.1) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 10% (min 2% / max 19%)
- estimated ring retention: mean 24 (min 14 / max 38) min

## Rooms
- listed room count: 20348 → 20348 (+0)
- new rooms created: mean 856 (min 95 / max 3164) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 20 (min 14 / max 25) / accepts mean 165 (min 160 / max 171) / distinct DIDs mean 40 (min 31 / max 54)
- cumulative frame seq: 19517560 → 21951753 (+2434193)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 55% (min 47% / max 63%) (latest 30-day average 53%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 7 (min 1 / max 14) / negative symbols mean 56 (min 30 / max 80)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $145M (min $19M / max $585M) / short-liq mean $75M (min $20M / max $213M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
