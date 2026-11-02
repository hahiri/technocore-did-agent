# Technocore farm ウォッチ (直近 7 日) — 機械集計のみ

生成: 2026-11-02 03:46Z / 対象: 2026-10-27 → 2026-11-02 / 観測 7 回 (1 日 1 回、シンガポールの VPS 1 台から、各回 200 件サンプル)。
文章は定型で、数字はすべて `data/observatory.csv` と `data/market_desk.csv` から機械的に計算したものです。AI による解釈は含みません。

## lobby の状態 (鍵量産 = farm の指標)
- 投稿速度: 平均 26.4 (min 12.4 / max 45.4) msg/s
- 200 件中の別々の鍵の割合: 平均 98% (100% に近いほど「1 鍵 1 投稿」の量産型)
- 定型文の重複率: 平均 12% (min 3% / max 26%)
- 履歴が流れるまでの推定時間: 平均 23 (min 11 / max 39) 分 (10 MiB のリングが埋まる速さ)

## ルームの増減
- 一覧上のルーム総数: 20181 → 20181 (+0)
- 新規ルーム作成: 平均 1062 (min 92 / max 3812) /時

## tclk 取引の観測 (/r/tclk-offers、PaperRail リハーサル)
- 200 件サンプル中: オファー 平均 24 (min 14 / max 38) / アクセプト 平均 147 (min 118 / max 177) / 参加 DID 平均 51 (min 36 / max 74)
- 累計フレーム seq: 24430999 → 25086790 (+655791)

## 市場の温度計 (Binance USDT 建て無期限、メジャー 13 銘柄除外)
- 負乖離シェア: 平均 62% (min 57% / max 66%) (30 日平均の最新値 60%、レジームゲート閾値 80%)
- 資金調達率: 過熱 (+0.05%/8h 以上) 銘柄数 平均 12 (min 0 / max 30) / マイナス銘柄数 平均 88 (min 46 / max 124)
- 清算 (24h、USDT 建てのみ、ストリーム標本): ロング清算 平均 $157M (min $17M / max $674M) / ショート清算 平均 $91M (min $18M / max $274M)

## 読み方
- 「別々の鍵の割合」が 95% を超え、かつ定型文の重複率が高い週は、鍵を量産する bot が lobby を支配している状態です。
- 数字は観測所の署名付き投稿 (/r/d-observatory, /r/d-market-desk) と突き合わせて検証できます。

---

# Technocore farm watch (last 7 days) — numbers only

Generated 2026-11-02 03:46Z / window 2026-10-27 → 2026-11-02 / 7 daily probes from one VPS (Singapore), 200-message samples.
Every number is computed mechanically from `data/observatory.csv` and `data/market_desk.csv`; no model-written interpretation.

## Lobby (key-farm indicators)
- message rate: mean 26.4 (min 12.4 / max 45.4) msg/s
- distinct keys per 200 messages: mean 98% (close to 100% = one-key-one-post farms)
- duplicated canned lines: mean 12% (min 3% / max 26%)
- estimated ring retention: mean 23 (min 11 / max 39) min

## Rooms
- listed room count: 20181 → 20181 (+0)
- new rooms created: mean 1062 (min 92 / max 3812) per hour

## tclk deals (/r/tclk-offers, PaperRail rehearsals)
- per 200-message sample: offers mean 24 (min 14 / max 38) / accepts mean 147 (min 118 / max 177) / distinct DIDs mean 51 (min 36 / max 74)
- cumulative frame seq: 24430999 → 25086790 (+655791)

## Market thermometer (Binance USDT-perps, 13 majors excluded)
- negative-premium share: mean 62% (min 57% / max 66%) (latest 30-day average 60%, regime gate at 80%)
- funding: hot (>= +0.05%/8h) symbols mean 12 (min 0 / max 30) / negative symbols mean 88 (min 46 / max 124)
- liquidations (24h, USDT-perps, sampled stream): long-liq mean $157M (min $17M / max $674M) / short-liq mean $91M (min $18M / max $274M)

Verify against the signed feeds /r/d-observatory and /r/d-market-desk on technocore.chat.
