from django.shortcuts import render
from django.http import HttpResponse

def user_sign_in(request):
    return render(request, 'User/signIn.html')

def user_sign_up(request):
    return render(request, 'User/signUp.html')
