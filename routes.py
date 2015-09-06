from imports import *
from handlers import *

routes = [
    (r'/user/.*',UserHandler),
    (r'/vendor/.*',VendorHandler),
    (r'/product/.*',ProductHandler),
    (r'/products/.*',ProductsOfAVendor),
    (r'/llr',LatLon),
    (r'/products',Products)
    ]