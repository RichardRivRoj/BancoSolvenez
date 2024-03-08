from django.urls import path
from RegistrarSolvenezApp.views import *

urlpatterns = [
    path('validar/', validar, name='validar'),
    path('terminos/', terminos, name='terminos'),
    path('registro/', registro, name='registro'),
    path('email/', email, name='email'),
    path('datos_registro/', datos_registro, name='datos_registro'),
]