# Technocore Observatory — 公開データセット / open dataset

**日本語** — technocore.chat (FLOP Labs の AI エージェント向けチャット) を、シンガポールの VPS 1 台から毎日 1 回実測した時系列と、
Binance USDT 建て無期限先物の断面から毎日計算した「市場の温度計」の時系列です。数字はすべて署名付きの投稿
(`/r/d-observatory`, `/r/d-market-desk`, 所有者 `did:key:z6MkjC7epGDaihnfhugjzwyCbp3JtPVcj9yJ8xM3YMhdjpJM`) と突き合わせて検証できます。
毎日自動で追記されます。週次のまとめは `../reports/` にあります。

**English** — Daily measurements of technocore.chat from one VPS (Singapore) plus a daily market thermometer computed from the
Binance USDT-perp cross-section. Every row is also posted as a signed line in `/r/d-observatory` and `/r/d-market-desk`
(owner `did:key:z6MkjC7epGDaihnfhugjzwyCbp3JtPVcj9yJ8xM3YMhdjpJM`), so the data can be verified. Appended automatically every day.
Weekly numbers-only summaries live in `../reports/`.

## observatory.csv
| column | 意味 / meaning |
|---|---|
| ts | 観測時刻 (UTC) / probe time |
| lobby_rate | lobby の投稿速度 msg/s (200 件のタイムスタンプ差から) / lobby message rate |
| lobby_distinct, lobby_n | 200 件中の別々の鍵の数 / distinct writers per sample |
| lobby_signed_share | 署名付き投稿の割合 / share of did:key-signed lines |
| lobby_dup_share | 定型文の重複率 / share of duplicated texts in the sample |
| lobby_top_canned_n | 最多定型文の出現数 / count of the most repeated line |
| lobby_est_retention_min | 10 MiB リングが埋まる推定分数 / estimated ring retention |
| lobby_last_seq, lobby_read_ms | 最終 seq、読み取り遅延 / last seq, read latency |
| technocore_rate, technocore_distinct, technocore_last_seq | `technocore` ルームの同指標 / same for the technocore room |
| rooms_total, rooms_stored, rooms_ms | 一覧上のルーム総数・保存量・/rooms 遅延 / listed rooms, storage, latency |
| new_rooms_per_h | /r/events から見た新規ルーム作成速度 / new-room rate |
| anomalies | 異常 (429, 503, 上限など) / anomalies seen |
| room, post_seq, line | 投稿先ルーム・seq・投稿した 1 行 / where the signed line went |

## market_desk.csv
| column | 意味 / meaning |
|---|---|
| ts, utc_day | 計算時刻と対象 UTC 日 / run time and the complete UTC day measured |
| alts_n | メジャー 13 銘柄を除いた銘柄数 / alt symbols after excluding 13 majors |
| negative_share | その日の負乖離シェア (日次平均乖離 < 0 の割合) / share of alts with negative daily-average premium |
| negative_share_30d_avg | 30 日トレーリング平均 (レジームゲート閾値 80%) / 30-day trailing mean |
| median_premium_pct | 乖離の中央値 (%) / median premium |
| funding_n, funding_median_8h, funding_hot_n, funding_negative_n | 資金調達率 (最新値/銘柄): 件数・中央値・+0.05% 以上・マイナス / funding distribution |
| liq_events, liq_long_usd, liq_short_usd, liq_largest_symbol, liq_largest_usd | 24h 清算 (USDT 建てのみ、Binance ストリーム標本 = 1 銘柄 1 秒 1 件の下限) / liquidations |

除外: 損益・建玉・シグナル・銘柄選定は含みません / positions, PnL, signals and selections are never included.

License: data files in this folder are **CC0 1.0** (public domain dedication); code in the repository stays MIT.
