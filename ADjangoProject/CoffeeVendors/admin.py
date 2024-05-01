from django.contrib import admin
from .models import CoffeeVendor, VendorType, CoffeeVendorReview

admin.site.register(CoffeeVendor)
admin.site.register(VendorType)
admin.site.register(CoffeeVendorReview)
