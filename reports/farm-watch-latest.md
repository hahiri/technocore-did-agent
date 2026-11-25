# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-11-25 03:47Z / 対象: 2026-11-19 → 2026-11-25 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 11.7 (min 5.7 / max 21.4) msg/s
- 200 件中の別々の鍵の割合: 平均 97% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 14% (min 0% / max 26%)
- 履歴が流れるまでの推定時間: 平均 55 (min 24 / max 90) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 53385 → 10580 (-42805)
- 新規ルーム作成: 平均 977 (min 91 / max 3139) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 29 (min 10 / max 46) / アクセプト 平均 83 (min 27 / max 125) / 参加 DID 平均 85 (min 46 / max 124)
- 累計フレーム seq: 25938229 → 26184563 (+246334)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 62% (min 58% / max 66%) (30 日平均の最新値 60%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 10 (min 0 / max 29) / マイナス銘柄数 平均 159 (min 102 / max 231)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $274M (min $66M / max $917M) / ショート清算 平均 $156M (min $59M / max $264M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-11-25 03:47Z / window 2026-11-19 → 2026-11-25 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 11.7 (min 5.7 / max 21.4) msg/s
- distinct keys per 200 messages: mean 97% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 14% (min 0% / max 26%)
- estimated ring retention: mean 55 (min 24 / max 90) min

## Rooms
- listed room count: 53385 → 10580 (-42805)
- new rooms created: mean 977 (min 91 / max 3139) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 29 (min 10 / max 46) / accepts mean 83 (min 27 / max 125) / distinct DIDs mean 85 (min 46 / max 124)
- cumulative frame seq: 25938229 → 26184563 (+246334)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 62% (min 58% / max 66%) (latest 30-day average 60%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 10 (min 0 / max 29) / negative symbols mean 159 (min 102 / max 231)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $274M (min $66M / max $917M) / short-liq mean $156M (min $59M / max $264M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
