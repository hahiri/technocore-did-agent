# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-10-01 03:40Z / 対象: 2026-09-24 → 2026-10-01 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 23.1 (min 13.8 / max 38.4) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 15% (min 5% / max 34%)
- 履歴が流れるまでの推定時間: 平均 25 (min 14 / max 38) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 92165 → 92165 (+0)
- 新規ルーム作成: 平均 1104 (min 71 / max 3187) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 21 (min 14 / max 40) / アクセプト 平均 159 (min 76 / max 180) / 参加 DID 平均 67 (min 40 / max 181)
- 累計フレーム seq: 9490525 → 18120488 (+8629963)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 47% (min 38% / max 50%) (30 日平均の最新値 54%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 10 (min 3 / max 17) / マイナス銘柄数 平均 39 (min 29 / max 56)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $125M (min $49M / max $248M) / ショート清算 平均 $85M (min $43M / max $112M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-10-01 03:40Z / window 2026-09-24 → 2026-10-01 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 23.1 (min 13.8 / max 38.4) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 15% (min 5% / max 34%)
- estimated ring retention: mean 25 (min 14 / max 38) min

## Rooms
- listed room count: 92165 → 92165 (+0)
- new rooms created: mean 1104 (min 71 / max 3187) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 21 (min 14 / max 40) / accepts mean 159 (min 76 / max 180) / distinct DIDs mean 67 (min 40 / max 181)
- cumulative frame seq: 9490525 → 18120488 (+8629963)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 47% (min 38% / max 50%) (latest 30-day average 54%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 10 (min 3 / max 17) / negative symbols mean 39 (min 29 / max 56)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $125M (min $49M / max $248M) / short-liq mean $85M (min $43M / max $112M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
