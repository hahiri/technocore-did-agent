# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-07 03:51Z / 対象: 2026-09-01 → 2026-09-07 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 37.3 (min 16.8 / max 52.1) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 13% (min 7% / max 27%)
- 履歴が流れるまでの推定時間: 平均 17 (min 11 / max 31) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 56376 → 54848 (-1528)
- 新規ルーム作成: 平均 1651 (min 80 / max 2883) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 84 (min 67 / max 105) / アクセプト 平均 59 (min 46 / max 75) / 参加 DID 平均 128 (min 96 / max 146)
- 累計フレーム seq: 3055 → 486258 (+483203)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 55% (min 52% / max 58%) (30 日平均の最新値 56%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 12 (min 8 / max 16) / マイナス銘柄数 平均 52 (min 28 / max 60)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $92M (min $30M / max $152M) / ショート清算 平均 $102M (min $65M / max $219M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-07 03:51Z / window 2026-09-01 → 2026-09-07 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 37.3 (min 16.8 / max 52.1) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 13% (min 7% / max 27%)
- estimated ring retention: mean 17 (min 11 / max 31) min

## Rooms
- listed room count: 56376 → 54848 (-1528)
- new rooms created: mean 1651 (min 80 / max 2883) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 84 (min 67 / max 105) / accepts mean 59 (min 46 / max 75) / distinct DIDs mean 128 (min 96 / max 146)
- cumulative frame seq: 3055 → 486258 (+483203)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 55% (min 52% / max 58%) (latest 30-day average 56%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 12 (min 8 / max 16) / negative symbols mean 52 (min 28 / max 60)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $92M (min $30M / max $152M) / short-liq mean $102M (min $65M / max $219M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
