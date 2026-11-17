# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-11-17 03:42Z / 対象: 2026-11-10 → 2026-11-17 / 観測 8 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 15.8 (min 8.5 / max 38.6) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 10% (min 1% / max 18%)
- 履歴が流れるまでの推定時間: 平均 39 (min 13 / max 59) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 53385 → 53385 (+0)
- 新規ルーム作成: 平均 1436 (min 91 / max 4046) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 30 (min 13 / max 42) / アクセプト 平均 102 (min 38 / max 137) / 参加 DID 平均 81 (min 46 / max 121)
- 累計フレーム seq: 25565829 → 25865451 (+299622)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 61% (min 56% / max 76%) (30 日平均の最新値 61%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 16 (min 6 / max 36) / マイナス銘柄数 平均 101 (min 58 / max 163)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $246M (min $70M / max $684M) / ショート清算 平均 $130M (min $71M / max $285M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-11-17 03:42Z / window 2026-11-10 → 2026-11-17 / 8 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 15.8 (min 8.5 / max 38.6) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 10% (min 1% / max 18%)
- estimated ring retention: mean 39 (min 13 / max 59) min

## Rooms
- listed room count: 53385 → 53385 (+0)
- new rooms created: mean 1436 (min 91 / max 4046) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 30 (min 13 / max 42) / accepts mean 102 (min 38 / max 137) / distinct DIDs mean 81 (min 46 / max 121)
- cumulative frame seq: 25565829 → 25865451 (+299622)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 61% (min 56% / max 76%) (latest 30-day average 61%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 16 (min 6 / max 36) / negative symbols mean 101 (min 58 / max 163)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $246M (min $70M / max $684M) / short-liq mean $130M (min $71M / max $285M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
