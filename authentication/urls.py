from django.urls import path
from .views import index
urlpatterns = [
    path('signin/', index, name='signin'),
]
