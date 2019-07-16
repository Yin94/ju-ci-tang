from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def auth(request):
    return render(request, 'auth/auth.html')
