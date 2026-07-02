import sys
import Quartz
from Foundation import NSURL

inp, outp, x, y, w, h = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:7])
ci = Quartz.CIImage.imageWithContentsOfURL_(NSURL.fileURLWithPath_(inp))
cropped = ci.imageByCroppingToRect_(Quartz.CGRectMake(x, y, w, h))
# translate so the output origin is (0,0)
moved = cropped.imageByApplyingTransform_(Quartz.CGAffineTransformMakeTranslation(-x, -y))
ctx = Quartz.CIContext.context()
cs = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceSRGB)
png = ctx.PNGRepresentationOfImage_format_colorSpace_options_(moved, Quartz.kCIFormatRGBA8, cs, None)
png.writeToFile_atomically_(outp, True)
print("ok")
