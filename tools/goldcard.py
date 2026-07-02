"""Regenerate the gold FUT-style card background.

Reuses the shield silhouette (alpha) from the existing asset, repaints the
gold finish (gradient + brushed streaks + highlight), draws a custom
"MLSYS 26" watermark instead of the baked-in FUT letters, and places the
lighter lower panel where the layout wants it.
"""
import random
import sys

import CoreText
import Quartz
from Foundation import NSURL, NSAttributedString

SRC, OUT = sys.argv[1], sys.argv[2]
W, H = 540, 820
PANEL_TOP_FROM_TOP = 0.585          # lower panel starts here (fraction of height)
PANEL_Y = H * (1 - PANEL_TOP_FROM_TOP)  # CG origin is bottom-left

random.seed(24)

# --- shield silhouette from the existing asset ---
src_ci = Quartz.CIImage.imageWithContentsOfURL_(NSURL.fileURLWithPath_(SRC))
cictx = Quartz.CIContext.context()
mask_cg = cictx.createCGImage_fromRect_(src_ci, src_ci.extent())

cs = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceSRGB)
ctx = Quartz.CGBitmapContextCreate(None, W, H, 8, W * 4, cs,
                                   Quartz.kCGImageAlphaPremultipliedLast)
Quartz.CGContextClipToMask(ctx, Quartz.CGRectMake(0, 0, W, H), mask_cg)


def gradient(colors, locs):
    flat = []
    for c in colors:
        flat.extend(c)
    return Quartz.CGGradientCreateWithColorComponents(cs, flat, locs, len(locs))


# --- base gold gradient (top light -> bottom rich) ---
base = gradient([
    (0.976, 0.930, 0.735, 1.0),
    (0.925, 0.815, 0.510, 1.0),
    (0.855, 0.700, 0.360, 1.0),
    (0.760, 0.585, 0.255, 1.0),
], [1.0, 0.62, 0.28, 0.0])
Quartz.CGContextDrawLinearGradient(ctx, base,
                                   Quartz.CGPointMake(W / 2, H),
                                   Quartz.CGPointMake(W / 2, 0), 0)

# --- brushed-metal streaks ---
for _ in range(2200):
    y = random.uniform(0, H)
    x = random.uniform(-40, W)
    ln = random.uniform(30, 220)
    a = random.uniform(0.012, 0.045)
    if random.random() < 0.5:
        Quartz.CGContextSetRGBFillColor(ctx, 1, 1, 1, a)
    else:
        Quartz.CGContextSetRGBFillColor(ctx, 0.45, 0.33, 0.10, a * 0.8)
    Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(x, y, ln, 1))

# --- soft radial highlight, upper center ---
hi = gradient([(1, 1, 1, 0.30), (1, 1, 1, 0.0)], [0.0, 1.0])
Quartz.CGContextDrawRadialGradient(ctx, hi,
                                   Quartz.CGPointMake(W / 2, H * 0.82), 0,
                                   Quartz.CGPointMake(W / 2, H * 0.82), W * 0.75, 0)


def draw_text(s, font_name, size, x, y, rgba, rotate_deg=0.0):
    font = CoreText.CTFontCreateWithName(font_name, size, None)
    color = Quartz.CGColorCreate(cs, rgba)
    astr = NSAttributedString.alloc().initWithString_attributes_(s, {
        CoreText.kCTFontAttributeName: font,
        CoreText.kCTForegroundColorAttributeName: color,
    })
    line = CoreText.CTLineCreateWithAttributedString(astr)
    Quartz.CGContextSaveGState(ctx)
    Quartz.CGContextTranslateCTM(ctx, x, y)
    if rotate_deg:
        Quartz.CGContextRotateCTM(ctx, rotate_deg * 3.14159265 / 180)
    Quartz.CGContextSetTextPosition(ctx, 0, 0)
    CoreText.CTLineDraw(line, ctx)
    Quartz.CGContextRestoreGState(ctx)


# --- custom watermark: MLSYS 26, upper zone only (like FUT's edition letters) ---
Quartz.CGContextSaveGState(ctx)
Quartz.CGContextClipToRect(ctx, Quartz.CGRectMake(0, PANEL_Y, W, H - PANEL_Y))
# darker embossed pass, then a light offset pass for the metal-etched feel
draw_text("MLSYS", "HelveticaNeue-CondensedBlack", 172, -30, PANEL_Y + 60,
          (0.42, 0.30, 0.08, 0.10), rotate_deg=8)
draw_text("MLSYS", "HelveticaNeue-CondensedBlack", 172, -28, PANEL_Y + 62,
          (1.0, 0.97, 0.85, 0.10), rotate_deg=8)
draw_text("26", "HelveticaNeue-CondensedBlack", 230, W - 175, PANEL_Y + 175,
          (0.42, 0.30, 0.08, 0.085), rotate_deg=8)
Quartz.CGContextRestoreGState(ctx)

# --- lighter lower panel ---
panel = gradient([
    (0.985, 0.945, 0.780, 0.92),
    (0.930, 0.835, 0.560, 0.55),
    (0.905, 0.790, 0.470, 0.80),
], [1.0, 0.45, 0.0])
Quartz.CGContextSaveGState(ctx)
Quartz.CGContextClipToRect(ctx, Quartz.CGRectMake(0, 0, W, PANEL_Y))
Quartz.CGContextDrawLinearGradient(ctx, panel,
                                   Quartz.CGPointMake(W / 2, PANEL_Y),
                                   Quartz.CGPointMake(W / 2, 0), 0)
Quartz.CGContextRestoreGState(ctx)
# seam: soft shadow just above the panel edge, thin highlight on it
Quartz.CGContextSetRGBFillColor(ctx, 0.40, 0.28, 0.08, 0.10)
Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(0, PANEL_Y, W, 3))
Quartz.CGContextSetRGBFillColor(ctx, 1, 1, 1, 0.35)
Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(0, PANEL_Y - 1.5, W, 1.5))

# --- inner edge glow to sell the bevel ---
edge = gradient([(1, 1, 1, 0.0), (1, 1, 1, 0.18)], [0.0, 1.0])
Quartz.CGContextDrawRadialGradient(ctx, edge,
                                   Quartz.CGPointMake(W / 2, H / 2), W * 0.30,
                                   Quartz.CGPointMake(W / 2, H / 2), W * 0.62, 0)

img = Quartz.CGBitmapContextCreateImage(ctx)
dest = Quartz.CGImageDestinationCreateWithURL(
    NSURL.fileURLWithPath_(OUT), "public.png", 1, None)
Quartz.CGImageDestinationAddImage(dest, img, None)
assert Quartz.CGImageDestinationFinalize(dest)
print("ok", OUT)
