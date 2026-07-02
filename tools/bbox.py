import sys
import Quartz
from Foundation import NSURL

ci = Quartz.CIImage.imageWithContentsOfURL_(NSURL.fileURLWithPath_(sys.argv[1]))
w, h = int(ci.extent().size.width), int(ci.extent().size.height)
ctx = Quartz.CIContext.context()
cg = ctx.createCGImage_fromRect_(ci, ci.extent())
provider = Quartz.CGImageGetDataProvider(cg)
data = Quartz.CGDataProviderCopyData(provider)
buf = bytes(data)
bpr = Quartz.CGImageGetBytesPerRow(cg)
# RGBA8: alpha at offset 3
minx, maxx, miny, maxy = w, 0, h, 0
for y in range(0, h, 2):
    row = y * bpr
    for x in range(0, w, 2):
        if buf[row + x * 4 + 3] > 40:
            if x < minx: minx = x
            if x > maxx: maxx = x
            if y < miny: miny = y
            if y > maxy: maxy = y
print(f"w={w} h={h} bbox x:[{minx},{maxx}] y:[{miny},{maxy}] cx={(minx+maxx)/2:.0f} cy={(miny+maxy)/2:.0f}")
