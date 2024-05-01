from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorsList.as_view(), name='vendors-list'),
    path('vendors/<int:pk>', views.VendorDetail.as_view(), name='vendors-by-id')

]
