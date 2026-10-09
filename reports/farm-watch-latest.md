# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-10-09 03:48Z / 対象: 2026-10-03 → 2026-10-09 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 25.5 (min 13.4 / max 38.1) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 10% (min 3% / max 19%)
- 履歴が流れるまでの推定時間: 平均 23 (min 14 / max 38) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 92165 → 20348 (-71817)
- 新規ルーム作成: 平均 975 (min 95 / max 3164) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 22 (min 14 / max 32) / アクセプト 平均 163 (min 156 / max 169) / 参加 DID 平均 43 (min 31 / max 57)
- 累計フレーム seq: 18917243 → 21646330 (+2729087)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 52% (min 46% / max 60%) (30 日平均の最新値 52%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 8 (min 4 / max 14) / マイナス銘柄数 平均 55 (min 30 / max 80)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $183M (min $19M / max $585M) / ショート清算 平均 $96M (min $20M / max $213M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-10-09 03:48Z / window 2026-10-03 → 2026-10-09 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 25.5 (min 13.4 / max 38.1) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 10% (min 3% / max 19%)
- estimated ring retention: mean 23 (min 14 / max 38) min

## Rooms
- listed room count: 92165 → 20348 (-71817)
- new rooms created: mean 975 (min 95 / max 3164) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 22 (min 14 / max 32) / accepts mean 163 (min 156 / max 169) / distinct DIDs mean 43 (min 31 / max 57)
- cumulative frame seq: 18917243 → 21646330 (+2729087)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 52% (min 46% / max 60%) (latest 30-day average 52%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 8 (min 4 / max 14) / negative symbols mean 55 (min 30 / max 80)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $183M (min $19M / max $585M) / short-liq mean $96M (min $20M / max $213M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
