from django.urls import path
from RegistrarSolvenezApp.views import *

urlpatterns = [
    path('validar/', validar, name='Validar'),
    path('terminos/', terminos, name='Terminos'),
    path('registro/', registro, name='Registro'),
    path('email/', email, name='Email'),
    path('datos_registro/', datos_registro, name='DatosR'),
]