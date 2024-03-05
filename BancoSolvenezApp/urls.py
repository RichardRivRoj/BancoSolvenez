from django.urls import path
from BancoSolvenezApp.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('sobre_nosotros/', sobre_nosotros, name='Sobre_nosotros'),
]