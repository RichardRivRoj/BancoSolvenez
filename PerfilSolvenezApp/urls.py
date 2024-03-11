
from django.urls import path
from PerfilSolvenezApp.views import *

urlpatterns = [
    path('login/', perfil, name='Perfil'),
    path('logout/', exit, name='exit'),
    path('movimientos/', movimientos, name='movimientos'),
    path('tranferencia/', transferencias, name='transferencias'),
]
