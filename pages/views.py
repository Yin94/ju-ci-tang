from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def signin(request):
    return render(request, 'auth/signin.html')


def signup(request):
    return render(request, 'auth/signup.html')
