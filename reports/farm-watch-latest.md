# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-26 03:41Z / 対象: 2026-09-19 → 2026-09-26 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 14.3 (min 7.9 / max 19.0) msg/s
- 200 件中の別々の鍵の割合: 平均 97% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 28% (min 6% / max 53%)
- 履歴が流れるまでの推定時間: 平均 39 (min 27 / max 66) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 92165 → 92165 (+0)
- 新規ルーム作成: 平均 906 (min 168 / max 1956) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 36 (min 17 / max 66) / アクセプト 平均 125 (min 76 / max 180) / 参加 DID 平均 96 (min 43 / max 181)
- 累計フレーム seq: 6713335 → 16436017 (+9722682)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 46% (min 35% / max 52%) (30 日平均の最新値 55%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 13 (min 3 / max 18) / マイナス銘柄数 平均 38 (min 29 / max 56)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $130M (min $78M / max $248M) / ショート清算 平均 $162M (min $79M / max $356M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-26 03:41Z / window 2026-09-19 → 2026-09-26 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 14.3 (min 7.9 / max 19.0) msg/s
- distinct keys per 200 messages: mean 97% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 28% (min 6% / max 53%)
- estimated ring retention: mean 39 (min 27 / max 66) min

## Rooms
- listed room count: 92165 → 92165 (+0)
- new rooms created: mean 906 (min 168 / max 1956) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 36 (min 17 / max 66) / accepts mean 125 (min 76 / max 180) / distinct DIDs mean 96 (min 43 / max 181)
- cumulative frame seq: 6713335 → 16436017 (+9722682)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 46% (min 35% / max 52%) (latest 30-day average 55%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 13 (min 3 / max 18) / negative symbols mean 38 (min 29 / max 56)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $130M (min $78M / max $248M) / short-liq mean $162M (min $79M / max $356M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
