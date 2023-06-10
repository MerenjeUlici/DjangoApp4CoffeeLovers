from django.shortcuts import render
from django.http import HttpResponse

def coffee_vendors_home_map(request):
    return render(request, 'CoffeeVendors/vendors_home_map.html')

def coffee_vendors_by_id_page(request):
    return render(request, 'CoffeeVendors/vendors_by_id_page.html')
