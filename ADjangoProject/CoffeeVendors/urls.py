from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_vendors_home_map, name='vendors-map'),
    path('vendor/', views.coffee_vendors_by_id_page, name='vendors-by-id')

]
