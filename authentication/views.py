from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import json
# Create your views here.


def index(request):

    data = json.loads(request.body)
    username = data['usr_name']
    password = data['pswd']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({'token': 'dasdasdasdasd'})
    else:
        return JsonResponse({'errors': [{'status': '401', 'message': 'Failed'}]})
