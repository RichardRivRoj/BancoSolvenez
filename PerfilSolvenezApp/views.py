from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def perfil(request):

    return render(request, 'PerfilSolvenezApp/perfil.html')

def exit(request):

    logout(request)
    return redirect('Inicio')

def base(request):

    return render(request, 'PerfilSolvenezApp/base.html')
