from django.shortcuts import render, redirect
from user.models import User
from .forms import NuevoUsuarioForm, ValidarForm
from django.contrib.auth import authenticate, login

# Create your views here.

def validar(request):

    data = {
        'formV': ValidarForm(),
    }
    return render(request, 'RegistrarSolvenezApp/validar.html', data)

def terminos(request):

    return render(request, 'RegistrarSolvenezApp/terminos.html')

def registro(request):

    data = {
        'formsR': NuevoUsuarioForm(),
    }
        
    return render(request, 'registration/registro.html', data)

def email(request):

    return render(request, 'RegistrarSolvenezApp/email.html')

def datos_registro(request):

    return render(request, 'RegistrarSolvenezApp/datos_registro.html')
