from django.urls import path, include
from . import views

urlpatterns = [
    path('signIn/', views.user_sign_in, name='user-sign-in'),
    path('signUp/', views.user_sign_up, name='user-sign-up'),
]
