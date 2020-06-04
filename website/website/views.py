from django.http import HttpResponse

def index(request):
    return HttpResponse("Main Page")

def login(request):
    return HttpResponse("Login Page")

def signup(request):
    return HttpResponse("Signup Page")
