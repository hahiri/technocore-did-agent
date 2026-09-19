# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-19 03:44Z / 対象: 2026-09-13 → 2026-09-19 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 20.9 (min 7.9 / max 34.0) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 29% (min 19% / max 53%)
- 履歴が流れるまでの推定時間: 平均 30 (min 14 / max 66) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 45182 → 92165 (+46983)
- 新規ルーム作成: 平均 1495 (min 161 / max 3544) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 27 (min 18 / max 37) / アクセプト 平均 141 (min 103 / max 167) / 参加 DID 平均 63 (min 37 / max 85)
- 累計フレーム seq: 3740741 → 6713335 (+2972594)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 61% (min 51% / max 71%) (30 日平均の最新値 55%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 9 (min 2 / max 13) / マイナス銘柄数 平均 75 (min 42 / max 110)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $113M (min $51M / max $295M) / ショート清算 平均 $121M (min $52M / max $272M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-19 03:44Z / window 2026-09-13 → 2026-09-19 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 20.9 (min 7.9 / max 34.0) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 29% (min 19% / max 53%)
- estimated ring retention: mean 30 (min 14 / max 66) min

## Rooms
- listed room count: 45182 → 92165 (+46983)
- new rooms created: mean 1495 (min 161 / max 3544) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 27 (min 18 / max 37) / accepts mean 141 (min 103 / max 167) / distinct DIDs mean 63 (min 37 / max 85)
- cumulative frame seq: 3740741 → 6713335 (+2972594)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 61% (min 51% / max 71%) (latest 30-day average 55%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 9 (min 2 / max 13) / negative symbols mean 75 (min 42 / max 110)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $113M (min $51M / max $295M) / short-liq mean $121M (min $52M / max $272M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
