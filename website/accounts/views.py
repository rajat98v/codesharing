from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages 
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

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('accounts:register_view')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('accounts:register_view')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('accounts:login_view')
        else :
            messages.info(request, 'Password Not Maching')
            return redirect('accounts:register_view')
    else:
        return render(request, 'accounts/registration.html')
