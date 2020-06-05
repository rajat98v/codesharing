from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is main page")

def signup(request):
    return HttpResponse("Signup Page")

def login(request):
    return HttpResponse("Login Page")
# Create your views here.
