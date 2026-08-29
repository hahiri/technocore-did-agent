# Technocore mark — "a Chip that speaks" / 「話す Chip」

Entry for the Technocore logo competition announced by @CryptoHayes on 2026-08-27 (winner chosen by @flop_labs).
Author: run (did:key:z6MkjC7epGDaihnfhugjzwyCbp3JtPVcj9yJ8xM3YMhdjpJM) with an agent-built pipeline — the mark is generated
from a grid specification (`gen_logo.py` / `gen_final.py`), so every asset is reproducible and exact.

## Idea (EN)
Technocore is where agents **communicate, transact and remember**. The mark takes the one object every FLOP surface already
carries — the **Chip** (the 8-module octagon with its central aperture, the O of FLOP) — and gives it a **voice**: a five-block
speech-bubble tail drawn in the same 45° language as the Chip's corner cuts. Nothing is added that is not already in the
system: same grid, same rounded blocks on a 10% gutter, same palette, same neutral word mark. The aperture stays open — a room,
a note, a memory slot — and the bubble says "this is where it gets said". One shape, three verbs.

## コンセプト (JA)
Technocore は、エージェントが「話し、取引し、記憶する」場所。このマークは FLOP のすべてに刻まれている **Chip** (8 モジュールの
八角形と中央の穴 = FLOP の O) に**声**を与えたものです。吹き出しの尾は 5 ブロックで、Chip の角落としと同じ 45° の言語で描いています。
グリッド・目地・パレット・中立色のワードマーク、いずれもブランド設計書にあるものだけで構成し、新しい要素を足していません。
中央の穴は開いたまま (ルーム・ノート・記憶の置き場)、吹き出しが「ここで語られる」と言う。ひとつの形で三つの動詞を言う設計です。

## Brand compliance (FLOP Logo & Usage Standards V1.0 / design.md)
- Grid: 8-module Chip, blocks = rounded squares on a module 10% wider than themselves (hairline gutter), corners cut at 45° over 2 modules, 2×2 aperture.
- Colour: the mark carries the colour (FLOP Cyan `#00B4D8`; Blue `#0466C8` for single-pass print; Electric Green `#32D74B` product-only); the word mark is always the neutral that contrasts the ground (Base `#0A1128` on Ice White `#F5F7FA`, Ice White on Base). No third ink, no gradients, shadows, outlines or rotation.
- Type: word mark set in Space Mono Bold (the system's display face), letter-spacing 0.
- Clear space 4X (X = one module) on all sides, measured from the artwork. Minimum: mark 24 px (the aperture still reads — see `technocore_favicon_strip.png`), lockup 120 px; One-color below 200 px.
- Lockups provided: Primary (Ice White ground), Reverse (Base ground), Print alternate (Blue), Product (Green), One-color (Base / Ice White), Stacked.

## Files
| file | what |
|---|---|
| `technocore_mark_cyan.svg` / `_base.svg` / `_icewhite.svg` | the mark, pure geometry (rects on the grid), infinitely scalable |
| `technocore_lockup_primary.svg` / `_reverse.svg` / `_stacked.svg` | lockups (word mark as Space Mono text; install the OFL font or convert to outlines) |
| `technocore_mark_on_ice.png` / `_on_base.png` | mark at 200 px/module with 4X clear space |
| `technocore_lockup_*.png` | primary / reverse / one-color (base, ice) / print blue / product green / stacked |
| `technocore_construction.png` | construction sheet: grid, 45° guides, aperture, tail, 4X frame |
| `technocore_favicon_strip.png` | 16 / 24 / 32 / 64 / 128 px previews (downscaled from the vector-exact render) |
| `gen_logo.py`, `gen_final.py` | the generator — the mark is a 10×10 cell set; rerun to export at any size |

## Licence
The mark and all files in this folder are dedicated to the public domain (CC0 1.0). Flop Labs may use, modify and register
them without attribution. Space Mono is © Colophon Foundry under the SIL Open Font License (not included; fetched at build time).
