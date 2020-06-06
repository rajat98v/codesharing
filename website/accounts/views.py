from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:index_view')

def loginme(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('accounts:index_view')
    else:
        return HttpResponse("Invalid Credentials")

def index_view(request):
    return render(request, 'accounts/index.html')
