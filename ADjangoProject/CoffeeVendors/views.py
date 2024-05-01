from rest_framework import generics
from .models import CoffeeVendor
from .serializers import CoffeeVendorSerializer

class VendorsList(generics.ListAPIView):
    queryset = CoffeeVendor.objects.all()
    serializer_class = CoffeeVendorSerializer


class VendorDetail(generics.RetrieveAPIView):
    queryset = CoffeeVendor.objects.all()
    serializer_class = CoffeeVendorSerializer
