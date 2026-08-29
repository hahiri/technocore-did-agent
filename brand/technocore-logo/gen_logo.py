#!/usr/bin/env python3
"""Technocore logo candidates on the FLOP pixel grid (8-module Chip: 45° corner cuts, central aperture) + a speech-bubble tail.
Outputs SVG (vector, geometry only) and PNG (PIL) for each candidate and lockup. Palette = FLOP canonical swatches only."""
from PIL import Image, ImageDraw, ImageFont
import os

BASE, ICE, CYAN, BLUE, GREEN = "#0A1128", "#F5F7FA", "#00B4D8", "#0466C8", "#32D74B"
FONT_B = "/root/technocore/logo/fonts/SpaceMono-Bold.ttf"
OUT = "/root/technocore/logo/out"; os.makedirs(OUT, exist_ok=True)

def octagon(n=8, cut=2):
    cells = set()
    for r in range(n):
        for c in range(n):
            if c + r < cut or (n-1-c) + r < cut or c + (n-1-r) < cut or (n-1-c) + (n-1-r) < cut:
                continue
            cells.add((c, r))
    return cells

def aperture(cells, size=2, n=8):
    o = (n - size) // 2
    for r in range(o, o+size):
        for c in range(o, o+size):
            cells.discard((c, r))
    return cells

CANDIDATES = {
    # A: Chip + 45° stair tail at bottom-left (the "voice" of the chip)
    "A_chip_bubble": aperture(octagon()) | {(1, 8), (0, 9), (2, 8) if False else (1, 8)} | {(1,7),(0,8),(0,9)},
    # A2: bolder tail (2-wide diagonal)
    "A2_chip_bubble_bold": aperture(octagon()) | {(1,7),(2,7),(0,8),(1,8),(0,9)},
    # B: Chip whose aperture is a horizontal message slot (4x1) + tail
    "B_chip_slot": (octagon() - {(2,3),(3,3),(4,3),(5,3)}) | {(1,7),(2,7),(0,8),(1,8),(0,9)},
}
# clean up A definition (set algebra above got clumsy)
CANDIDATES["A_chip_bubble"] = aperture(octagon()) | {(1,7),(0,8),(0,9)}

def bbox(cells):
    cs=[c for c,_ in cells]; rs=[r for _,r in cells]
    return min(cs), min(rs), max(cs), max(rs)

def svg_icon(cells, color, m=100, gutter=0.10, rx=0.18):
    c0,r0,c1,r1 = bbox(cells); W=(c1-c0+1)*m; H=(r1-r0+1)*m
    s=m*(1-gutter); off=m*gutter/2
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    for (c,r) in sorted(cells):
        x=(c-c0)*m+off; y=(r-r0)*m+off
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s*rx:.1f}" fill="{color}"/>')
    parts.append('</svg>'); return "\n".join(parts), W, H

def draw_cells(img, cells, color, m, ox, oy, gutter=0.10, rx=0.18):
    d=ImageDraw.Draw(img); c0,r0,_,_=bbox(cells); s=m*(1-gutter); off=m*gutter/2
    for (c,r) in cells:
        x=ox+(c-c0)*m+off; y=oy+(r-r0)*m+off
        d.rounded_rectangle([x,y,x+s,y+s], radius=s*rx, fill=color)

def png_icon(cells, color, ground, m=100, pad=None):
    c0,r0,c1,r1=bbox(cells); cw=(c1-c0+1); ch=(r1-r0+1)
    pad = pad if pad is not None else 4*m   # 4X clear space
    W=cw*m+2*pad; H=ch*m+2*pad
    img=Image.new("RGB",(W,H),ground); draw_cells(img,cells,color,m,pad,pad); return img

def png_lockup(cells, icon_color, text_color, ground, m=60, text="TECHNOCORE", stacked=False):
    c0,r0,c1,r1=bbox(cells); cw=(c1-c0+1); ch=(r1-r0+1); pad=4*m
    font=ImageFont.truetype(FONT_B, int(m*2.1)); tw=font.getlength(text); th=int(m*2.1)
    gap=int(m*1.5)
    if stacked:
        W=int(max(cw*m,tw)+2*pad); H=int(ch*m+gap+th+2*pad)
        img=Image.new("RGB",(W,H),ground); ox=(W-cw*m)//2; draw_cells(img,cells,icon_color,m,ox,pad)
        ImageDraw.Draw(img).text(((W-tw)//2, pad+ch*m+gap), text, font=font, fill=text_color)
    else:
        W=int(cw*m+gap+tw+2*pad); H=int(ch*m+2*pad)
        img=Image.new("RGB",(W,H),ground); draw_cells(img,cells,icon_color,m,pad,pad)
        oct_h=8*m; ty=pad+(oct_h-th)//2
        ImageDraw.Draw(img).text((pad+cw*m+gap, ty), text, font=font, fill=text_color)
    return img

for name, cells in CANDIDATES.items():
    svg,_,_=svg_icon(cells, CYAN); open(f"{OUT}/{name}_icon_cyan.svg","w").write(svg)
    png_icon(cells, CYAN, ICE).save(f"{OUT}/{name}_icon_on_ice.png")
    png_icon(cells, CYAN, BASE).save(f"{OUT}/{name}_icon_on_base.png")
    png_lockup(cells, CYAN, BASE, ICE).save(f"{OUT}/{name}_lockup_primary.png")     # Primary: Base word mark + Cyan chip on Ice
    png_lockup(cells, CYAN, ICE, BASE).save(f"{OUT}/{name}_lockup_reverse.png")     # Reverse: Ice White word mark + Cyan chip on Base
    png_lockup(cells, BASE, BASE, ICE).save(f"{OUT}/{name}_lockup_onecolor.png")    # One-color
    png_lockup(cells, CYAN, BASE, ICE, stacked=True).save(f"{OUT}/{name}_lockup_stacked.png")
    # small-size check (24 px chip) — the aperture must still read
    png_icon(cells, CYAN, ICE, m=3, pad=6).save(f"{OUT}/{name}_icon_24px.png")
print("\n".join(sorted(os.listdir(OUT))))
