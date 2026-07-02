import sys
import Vision
import Quartz
from Foundation import NSURL

inp, outp = sys.argv[1], sys.argv[2]
ci = Quartz.CIImage.imageWithContentsOfURL_(NSURL.fileURLWithPath_(inp))
assert ci is not None, "failed to load input image"

req = Vision.VNGenerateForegroundInstanceMaskRequest.alloc().init()
handler = Vision.VNImageRequestHandler.alloc().initWithCIImage_options_(ci, None)
ok, err = handler.performRequests_error_([req], None)
assert ok, f"vision request failed: {err}"

results = req.results()
assert results and len(results) > 0, "no foreground subject found"
res = results[0]

buf, err = res.generateMaskedImageOfInstances_fromRequestHandler_croppedToInstancesExtent_error_(
    res.allInstances(), handler, False, None
)
assert buf is not None, f"masking failed: {err}"

masked = Quartz.CIImage.imageWithCVPixelBuffer_(buf)
ctx = Quartz.CIContext.context()
cs = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceSRGB)
png = ctx.PNGRepresentationOfImage_format_colorSpace_options_(
    masked, Quartz.kCIFormatRGBA8, cs, None
)
assert png is not None, "png encode failed"
png.writeToFile_atomically_(outp, True)
print("ok", outp)
