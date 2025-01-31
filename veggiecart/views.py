from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.

def index(request):

    return render(request,'veggiecart/homepage/index.html')


def homepage(request):

    return render(request,'veggiecart/homepage/admin/index.html')

def signout(request):
    logout(request)
    
    return redirect('/')


def google_login(request):
    return render(request,'veggiecart/account/login.html')