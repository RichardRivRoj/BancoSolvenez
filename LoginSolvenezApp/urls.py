from django.urls import path
from LoginSolvenezApp.views import *

urlpatterns = [
    path('login/', login, name='Login'),
]