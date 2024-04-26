from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
from django.contrib.auth.models import User


class VendorType(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CoffeeVendor(models.Model):

    name = models.CharField(max_length=100)
    vendor_type = models.ForeignKey(VendorType, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 
    # rating =  
    # latitude =  
    # longitude =  
    # location = models.PointField(geography=True, default=Point(0.0, 0.0))

    def __str__(self):
        return self.name


class CoffeeVendorReview(models.Model):

    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )
    value = models.IntegerField(choices=RATING_CHOICES, default=1)
    coffee_vendor = models.ForeignKey(CoffeeVendor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1024)

    def __str__(self):
        coffee_vendor_name = CoffeeVendor.objects.get(pk=self.coffee_vendor.id)
        return f"{coffee_vendor_name} {self.value} from {self.user}" 
