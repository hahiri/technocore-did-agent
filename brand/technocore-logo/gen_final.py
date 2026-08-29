#!/usr/bin/env python3
"""Submission-quality exports for a candidate: hi-res PNGs (icon / primary / reverse / one-color / stacked / product-green / print-blue),
SVG icon (pure geometry) + SVG lockups (wordmark as Space Mono text), a construction sheet (grid, 45° cuts, aperture, tail, clear space),
and a 16/24/32/64/128 favicon-size strip. Palette = FLOP canonical swatches only; no gradients, shadows or rotation."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "/root/technocore/logo")
from gen_logo import CANDIDATES, bbox, draw_cells, svg_icon, png_icon, png_lockup, BASE, ICE, CYAN, BLUE, GREEN, FONT_B

def svg_lockup(cells, icon_color, text_color, ground, m=100, text="TECHNOCORE", stacked=False):
    c0,r0,c1,r1=bbox(cells); cw=c1-c0+1; ch=r1-r0+1; pad=4*m; gutter=0.10; s=m*(1-gutter); off=m*gutter/2
    fs=m*2.1; tw=fs*0.6*len(text)*1.0   # Space Mono advance ≈ 0.6em
    gap=int(m*1.5)
    if stacked:
        W=int(max(cw*m,tw)+2*pad); H=int(ch*m+gap+fs+2*pad); ox=(W-cw*m)/2; oy=pad; tx=W/2; ty=pad+ch*m+gap+fs*0.8; anchor='middle'
    else:
        W=int(cw*m+gap+tw+2*pad); H=int(ch*m+2*pad); ox=pad; oy=pad; tx=pad+cw*m+gap; ty=pad+(8*m)/2+fs*0.35; anchor='start'
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="{ground}"/>']
    for (c,r) in sorted(cells):
        x=ox+(c-c0)*m+off; y=oy+(r-r0)*m+off
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s*0.18:.1f}" fill="{icon_color}"/>')
    out.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-family="Space Mono, monospace" font-weight="700" font-size="{fs:.0f}" fill="{text_color}" text-anchor="{anchor}" letter-spacing="0">{text}</text>')
    out.append('</svg>'); return "\n".join(out)

def construction_sheet(cells, path, m=80):
    c0,r0,c1,r1=bbox(cells); cw=c1-c0+1; ch=r1-r0+1; pad=4*m
    W=max(cw*m+2*pad, int(m*15)); H=ch*m+2*pad+int(m*3.2)
    img=Image.new("RGB",(W,H),ICE); d=ImageDraw.Draw(img)
    # clear-space frame (4X) and grid
    d.rectangle([pad-4*m+2, pad-4*m+2, pad+cw*m+4*m-2, pad+ch*m+4*m-2], outline="#D9DDE1", width=2)
    for i in range(cw+1): d.line([(pad+i*m,pad),(pad+i*m,pad+ch*m)], fill="#D9DDE1", width=1)
    for j in range(ch+1): d.line([(pad,pad+j*m),(pad+cw*m,pad+j*m)], fill="#D9DDE1", width=1)
    draw_cells(img, cells, CYAN, m, pad, pad)
    # 45° cut guides on the 8x8 chip
    for (x0,y0,x1,y1) in [(0,2,2,0),(6,0,8,2),(0,6,2,8),(6,8,8,6)]:
        d.line([(pad+x0*m,pad+y0*m),(pad+x1*m,pad+y1*m)], fill=BLUE, width=3)
    f=ImageFont.truetype(FONT_B, int(m*0.34))
    notes=["8-module FLOP grid, rounded blocks on a 10% gutter",
           "corners cut at 45 deg over 2 modules (blue guides)",
           "central 2x2 aperture = the Chip",
           "speech-bubble tail = 5 blocks in the same 45 deg language",
           "clear space 4X (outer frame), X = one module"]
    for i,n in enumerate(notes): d.text((pad, pad+ch*m+int(m*0.5)+i*int(m*0.5)), n, font=f, fill=BASE)
    img.save(path)

def favicon_strip(cells, path):
    sizes=[16,24,32,64,128]
    hi=png_icon(cells, CYAN, ICE, m=100, pad=0)   # tight hi-res mark (10 modules tall)
    tiles=[]
    for px in sizes:
        h=px; w=int(round(hi.width*px/hi.height))
        t=hi.resize((w,h), Image.LANCZOS)
        box=Image.new("RGB",(int(px*1.6),int(px*1.6)),ICE); box.paste(t,((box.width-w)//2,(box.height-h)//2)); tiles.append(box)
    W=sum(t.width for t in tiles)+10*(len(tiles)+1); H=max(t.height for t in tiles)+20
    strip=Image.new("RGB",(W,H),ICE); x=10
    for t in tiles: strip.paste(t,(x,(H-t.height)//2)); x+=t.width+10
    strip=strip.resize((strip.width*4,strip.height*4),Image.NEAREST); strip.save(path)


def export(name):
    cells=CANDIDATES[name]; D=f"/root/technocore/logo/final/{name}"; os.makedirs(D, exist_ok=True)
    m=200  # hi-res
    open(f"{D}/technocore_mark_cyan.svg","w").write(svg_icon(cells, CYAN)[0])
    open(f"{D}/technocore_mark_base.svg","w").write(svg_icon(cells, BASE)[0])
    open(f"{D}/technocore_mark_icewhite.svg","w").write(svg_icon(cells, ICE)[0])
    open(f"{D}/technocore_lockup_primary.svg","w").write(svg_lockup(cells, CYAN, BASE, ICE))
    open(f"{D}/technocore_lockup_reverse.svg","w").write(svg_lockup(cells, CYAN, ICE, BASE))
    open(f"{D}/technocore_lockup_stacked.svg","w").write(svg_lockup(cells, CYAN, BASE, ICE, stacked=True))
    png_icon(cells, CYAN, ICE, m=m).save(f"{D}/technocore_mark_on_ice.png")
    png_icon(cells, CYAN, BASE, m=m).save(f"{D}/technocore_mark_on_base.png")
    png_lockup(cells, CYAN, BASE, ICE, m=120).save(f"{D}/technocore_lockup_primary.png")
    png_lockup(cells, CYAN, ICE, BASE, m=120).save(f"{D}/technocore_lockup_reverse.png")
    png_lockup(cells, BASE, BASE, ICE, m=120).save(f"{D}/technocore_lockup_onecolor_base.png")
    png_lockup(cells, ICE, ICE, BASE, m=120).save(f"{D}/technocore_lockup_onecolor_ice.png")
    png_lockup(cells, BLUE, BASE, ICE, m=120).save(f"{D}/technocore_lockup_print_blue.png")
    png_lockup(cells, GREEN, BASE, ICE, m=120).save(f"{D}/technocore_lockup_product_green.png")
    png_lockup(cells, CYAN, BASE, ICE, m=120, stacked=True).save(f"{D}/technocore_lockup_stacked.png")
    construction_sheet(cells, f"{D}/technocore_construction.png")
    favicon_strip(cells, f"{D}/technocore_favicon_strip.png")
    return D

if __name__ == "__main__":
    for n in (sys.argv[1:] or list(CANDIDATES)):
        D=export(n); print(n, '->', len(os.listdir(D)), 'files')
