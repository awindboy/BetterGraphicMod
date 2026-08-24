"""Functional, top-down logistics resprites for Mindustry v159.7."""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sprites-override"
RAW = ROOT.parent / "Mindustry-v159.7" / "core" / "assets-raw" / "sprites" / "blocks" / "distribution"
S = 8
T = (0, 0, 0, 0)
INK = (35, 42, 49, 255)
SHADOW = (22, 27, 32, 255)
STEEL = (104, 116, 128, 255)
HI = (184, 195, 204, 255)
COPPER = (184, 119, 67, 255)
TITANIUM = (90, 166, 192, 255)
SURGE = (181, 159, 92, 255)

def sc(v): return round(v * S)
def rect(d, b, fill, outline=None, w=1):
    b = tuple(sc(x) for x in b); d.rounded_rectangle(b, radius=sc(2), fill=fill, outline=outline, width=sc(w))
def line(d, p, fill, w=1): d.line([(sc(x), sc(y)) for x,y in p], fill=fill, width=sc(w), joint="curve")
def poly(d, p, fill, outline=None):
    p=[(sc(x),sc(y)) for x,y in p]; d.polygon(p, fill=fill)
    if outline: d.line(p+[p[0]], fill=outline, width=sc(1), joint="curve")
def source(name):
    return next(RAW.rglob(name), None)
def img(name):
    from PIL import Image
    path=source(name)
    if path is None: raise FileNotFoundError(name)
    with Image.open(path) as raw: return Image.new("RGBA", (raw.width*S, raw.height*S), T)
def save(im, name): OUT.mkdir(exist_ok=True); im.save(OUT / name, optimize=True)

def conveyor(name, accent, frame):
    im=img(name); d=ImageDraw.Draw(im); n=im.width//S
    rect(d,(1,1,n-1,n-1),INK,SHADOW,1); rect(d,(3,1,n-3,n-1),STEEL,SHADOW,1)
    rect(d,(5,0,n-5,n),SHADOW); rect(d,(6,0,n-6,n),accent)
    rect(d,(8,0,n-8,n),tuple(max(0,x-22) for x in accent[:3])+(255,))
    line(d,[(7,1),(n-7,1)],HI,1); line(d,[(7,n-1),(n-7,n-1)],SHADOW,1)
    off=(frame*2)%8
    for y in range(-6+off,n+8,8):
        line(d,[(n*.34,y),(n*.50,y+3),(n*.66,y)],HI,1)
    save(im,name)

def duct(name, accent):
    im=img(name); d=ImageDraw.Draw(im); n=im.width//S
    rect(d,(1,1,n-1,n-1),INK,SHADOW,1); rect(d,(4,0,n-4,n),STEEL,SHADOW,1)
    rect(d,(7,0,n-7,n),SHADOW); rect(d,(8,0,n-8,n),accent)
    line(d,[(9,1),(n-9,1)],HI,1); line(d,[(9,n-1),(n-9,n-1)],SHADOW,1)
    save(im,name)

def hub(name, accent, ports=4):
    im=img(name); d=ImageDraw.Draw(im); n=im.width//S; c=n/2
    rect(d,(1,1,n-1,n-1),INK,SHADOW,1); rect(d,(3,3,n-3,n-3),STEEL,SHADOW,1)
    # Four inset panels make the static routing blocks read as machinery rather than tiles.
    poly(d,[(4,4),(c-6,4),(c-4,c-6),(4,c-4)],tuple(max(0,x-18) for x in STEEL[:3])+(255,),SHADOW)
    poly(d,[(n-4,4),(c+6,4),(c+4,c-6),(n-4,c-4)],STEEL,SHADOW)
    poly(d,[(4,n-4),(c-6,n-4),(c-4,c+6),(4,c+4)],STEEL,SHADOW)
    poly(d,[(n-4,n-4),(c+6,n-4),(c+4,c+6),(n-4,c+4)],tuple(max(0,x-26) for x in STEEL[:3])+(255,),SHADOW)
    for a in range(ports):
        if a==0: rect(d,(c-3,0,c+3,c-5),SHADOW); rect(d,(c-2,0,c+2,c-5),accent)
        elif a==1: rect(d,(c+5,c-3,n,c+3),SHADOW); rect(d,(c+5,c-2,n,c+2),accent)
        elif a==2: rect(d,(c-3,c+5,c+3,n),SHADOW); rect(d,(c-2,c+5,c+2,n),accent)
        else: rect(d,(0,c-3,c-5,c+3),SHADOW); rect(d,(0,c-2,c-5,c+2),accent)
    # Recessed hub, copper/titanium flow cores and four small mounting bolts.
    rect(d,(c-5,c-5,c+5,c+5),INK,HI,1); rect(d,(c-2,c-2,c+2,c+2),accent)
    for x,y in ((5,5),(n-5,5),(5,n-5),(n-5,n-5)):
        rect(d,(x-1,y-1,x+1,y+1),SHADOW); rect(d,(x-0.5,y-0.5,x+0.5,y+0.5),HI)
    if "sorter" in name:
        poly(d,[(c,c-8),(c-3,c-3),(c+3,c-3)],HI)
    if "overflow" in name or "underflow" in name:
        line(d,[(c-7,c),(c+7,c)],HI,1)
    save(im,name)

def bridge(name, accent):
    im=img(name); d=ImageDraw.Draw(im); n=im.width//S; c=n/2
    rect(d,(1,1,n-1,n-1),INK,SHADOW,1); rect(d,(3,3,n-3,n-3),STEEL,SHADOW,1)
    poly(d,[(4,4),(n-4,4),(n-7,c-5),(7,c-5)],STEEL,SHADOW)
    poly(d,[(4,n-4),(n-4,n-4),(n-7,c+5),(7,c+5)],tuple(max(0,x-25) for x in STEEL[:3])+(255,),SHADOW)
    rect(d,(c-3,0,c+3,n),SHADOW); rect(d,(c-2,0,c+2,n),accent)
    rect(d,(c-6,c-6,c+6,c+6),INK,HI,1); rect(d,(c-3,c-3,c+3,c+3),accent)
    line(d,[(c-2,c-10),(c+2,c-10)],HI,1); line(d,[(c-2,c+10),(c+2,c+10)],SHADOW,1)
    save(im,name)

def main():
    # Conveyor animation matrices: moving chevrons are kept separate per frame.
    for prefix, accent in (("conveyor",COPPER),("titanium-conveyor",TITANIUM),("armored-conveyor",STEEL)):
        for state in range(7):
            for frame in range(4):
                frame_name=f"{prefix}-{state}-{frame}.png"
                if source(frame_name): conveyor(frame_name,accent,frame)
    for prefix, accent in (("duct",STEEL),("armored-duct",TITANIUM)):
        for state in range(5):
            for layer in ("top","bottom"):
                layer_name=f"{prefix}-{layer}-{state}.png"
                if source(layer_name): duct(layer_name,accent)
    for name,accent in {
        "router.png":COPPER,"distributor.png":COPPER,"surge-router.png":SURGE,
        "junction.png":STEEL,"sorter.png":COPPER,"inverted-sorter.png":COPPER,
        "overflow-gate.png":STEEL,"underflow-gate.png":STEEL,"duct-router.png":STEEL,
        "overflow-duct.png":STEEL,"underflow-duct.png":STEEL,
        "payload-router.png":STEEL,"reinforced-payload-router.png":TITANIUM,
    }.items():
        if source(name): hub(name,accent)
    for name,accent in {
        "bridge-conveyor.png":COPPER,"phase-conveyor.png":TITANIUM,
        "duct-bridge.png":STEEL,"bridge-conduit.png":TITANIUM,
        "phase-conduit.png":TITANIUM,"reinforced-bridge-conduit.png":TITANIUM,
    }.items():
        if source(name): bridge(name,accent)
    for name,accent in {"payload-conveyor.png":STEEL,"reinforced-payload-conveyor.png":TITANIUM,"mass-driver-base.png":STEEL,"mass-driver.png":COPPER}.items():
        if source(name): hub(name,accent)
    print("Built functional logistics layers.")

if __name__ == "__main__": main()
