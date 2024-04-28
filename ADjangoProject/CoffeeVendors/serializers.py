from rest_framework import serializers
from .models import CoffeeVendor


class CoffeeVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeVendor
        fields = ('id', 'name', 'vendor_type', 'user')