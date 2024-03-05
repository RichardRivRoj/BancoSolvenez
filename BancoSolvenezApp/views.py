from django.shortcuts import render

# Create your views here.


def inicio(request):

    return render(request, 'BancoSolvenezApp/inicio.html')

def sobre_nosotros(request):

    return render(request, 'BancoSolvenezApp/sobre_nosotros.html')


