# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-11-19 03:42Z / 対象: 2026-11-12 → 2026-11-19 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 14.5 (min 7.3 / max 38.6) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 12% (min 1% / max 26%)
- 履歴が流れるまでの推定時間: 平均 44 (min 13 / max 67) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 53385 → 53385 (+0)
- 新規ルーム作成: 平均 973 (min 91 / max 3904) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 29 (min 13 / max 46) / アクセプト 平均 93 (min 38 / max 137) / 参加 DID 平均 85 (min 46 / max 121)
- 累計フレーム seq: 25636186 → 25938229 (+302043)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 61% (min 56% / max 76%) (30 日平均の最新値 61%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 15 (min 6 / max 36) / マイナス銘柄数 平均 112 (min 68 / max 163)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $242M (min $70M / max $684M) / ショート清算 平均 $127M (min $72M / max $285M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-11-19 03:42Z / window 2026-11-12 → 2026-11-19 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 14.5 (min 7.3 / max 38.6) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 12% (min 1% / max 26%)
- estimated ring retention: mean 44 (min 13 / max 67) min

## Rooms
- listed room count: 53385 → 53385 (+0)
- new rooms created: mean 973 (min 91 / max 3904) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 29 (min 13 / max 46) / accepts mean 93 (min 38 / max 137) / distinct DIDs mean 85 (min 46 / max 121)
- cumulative frame seq: 25636186 → 25938229 (+302043)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 61% (min 56% / max 76%) (latest 30-day average 61%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 15 (min 6 / max 36) / negative symbols mean 112 (min 68 / max 163)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $242M (min $70M / max $684M) / short-liq mean $127M (min $72M / max $285M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
