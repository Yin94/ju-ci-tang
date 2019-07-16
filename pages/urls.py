from django.urls import path
from .views import index, signin, signup
urlpatterns = [
    path('', index, name='index'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
]
