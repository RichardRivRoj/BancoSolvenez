from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from user.models import User, Cuenta
from django.db.models import Sum
from .utils import transferir_fondos
import random
from .forms import TransaccionForm
from django.db import connection
from .models import Movimientos
from django.db.models import Q
# Create your views here.

@login_required
def perfil(request):

    usuario = request.user

    cuentas_usuario = Cuenta.objects.filter(user_fk_id=usuario)

    saldo_total = cuentas_usuario.aggregate(saldo_total=Sum('saldo'))['saldo_total'] or 0.00

    return render(request, 'PerfilSolvenezApp/perfil.html', {'usuario':usuario, 'cuentas':cuentas_usuario, 'saldo_total':saldo_total})

def exit(request):

    logout(request)
    return redirect('Inicio')


def transferencias(request):


    if request.method == 'POST':

        formsT = TransaccionForm(request.POST)

        if formsT.is_valid():

            referencia = str(random.randint(1000000000000,9999999999999))
            descripcion = 'TRANSFERENCIAS A TERCEROS'
            tipo_transaccion = 'DÉBITO'
            emisor = formsT.cleaned_data['emisor_fk'].id
            receptor = formsT.cleaned_data['receptor_fk'].id
            monto = formsT.cleaned_data['monto']
            
            with connection.cursor() as cursor:
                cursor.callproc('transferir_fondos', [
                    referencia,
                    descripcion,
                    tipo_transaccion,
                    emisor,
                    receptor,
                    monto,
                ])

            HttpResponse('Transferencia realizada correctamente')
    else:
        formsT = TransaccionForm()
        
    return render(request, 'PerfilSolvenezApp/transferencias.html', {'formsT':formsT})

def movimientos(request):

    usuario = request.user

    cuentas_usuario = Cuenta.objects.filter(user_fk_id=usuario)

    movimientos = Movimientos.objects.get(Q(emisor_fk_id=cuentas_usuario) | Q(receptor_fk_id=cuentas_usuario))
    movimientos = movimientos.order_by('-fecha')
    context = {'movimientos': movimientos}

    return render(request, 'PerfilSolvenezApp/movimientos.html', context)
