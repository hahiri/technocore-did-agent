# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-08-29 03:58Z / 対象: 2026-08-26 → 2026-08-29 / 観測 4 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 39.2 (min 25.5 / max 50.6) msg/s
- 200 件中の別々の鍵の割合: 平均 99% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 34% (min 4% / max 64%)
- 履歴が流れるまでの推定時間: 平均 21 (min 16 / max 31) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 8327 → 38211 (+29884)
- 新規ルーム作成: 平均 117 (min 59 / max 193) /時

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 54% (min 51% / max 56%) (30 日平均の最新値 58%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 6 (min 3 / max 7) / マイナス銘柄数 平均 49 (min 45 / max 54)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $132M (min $96M / max $179M) / ショート清算 平均 $123M (min $78M / max $159M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-08-29 03:58Z / window 2026-08-26 → 2026-08-29 / 4 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 39.2 (min 25.5 / max 50.6) msg/s
- distinct keys per 200 messages: mean 99% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 34% (min 4% / max 64%)
- estimated ring retention: mean 21 (min 16 / max 31) min

## Rooms
- listed room count: 8327 → 38211 (+29884)
- new rooms created: mean 117 (min 59 / max 193) per hour

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 54% (min 51% / max 56%) (latest 30-day average 58%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 6 (min 3 / max 7) / negative symbols mean 49 (min 45 / max 54)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $132M (min $96M / max $179M) / short-liq mean $123M (min $78M / max $159M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
