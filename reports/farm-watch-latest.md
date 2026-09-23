# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-09-23 03:48Z / 対象: 2026-09-17 → 2026-09-23 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 16.9 (min 7.9 / max 34.0) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 30% (min 19% / max 53%)
- 履歴が流れるまでの推定時間: 平均 36 (min 14 / max 66) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 92165 → 92165 (+0)
- 新規ルーム作成: 平均 928 (min 205 / max 1956) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 38 (min 23 / max 66) / アクセプト 平均 123 (min 98 / max 146) / 参加 DID 平均 88 (min 62 / max 135)
- 累計フレーム seq: 5575023 → 8880773 (+3305750)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 52% (min 35% / max 61%) (30 日平均の最新値 55%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 12 (min 6 / max 18) / マイナス銘柄数 平均 52 (min 29 / max 110)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $129M (min $55M / max $295M) / ショート清算 平均 $164M (min $79M / max $356M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-09-23 03:48Z / window 2026-09-17 → 2026-09-23 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 16.9 (min 7.9 / max 34.0) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 30% (min 19% / max 53%)
- estimated ring retention: mean 36 (min 14 / max 66) min

## Rooms
- listed room count: 92165 → 92165 (+0)
- new rooms created: mean 928 (min 205 / max 1956) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 38 (min 23 / max 66) / accepts mean 123 (min 98 / max 146) / distinct DIDs mean 88 (min 62 / max 135)
- cumulative frame seq: 5575023 → 8880773 (+3305750)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 52% (min 35% / max 61%) (latest 30-day average 55%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 12 (min 6 / max 18) / negative symbols mean 52 (min 29 / max 110)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $129M (min $55M / max $295M) / short-liq mean $164M (min $79M / max $356M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
