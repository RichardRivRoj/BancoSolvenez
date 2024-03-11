from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from user.models import User, Cuenta
from django.db.models import Sum
from .utils import transferir_fondos
import random
from .forms import TransaccionForm
from django.db import connection, transaction
from .models import Movimientos
from django.db.models import Q
from datetime import datetime
from decimal import Decimal
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

@transaction.atomic
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

    usuario_actual = request.user

    cuentas_usuario = usuario_actual.cuenta_set.filter()

    movimientos = Movimientos.objects.filter(Q(emisor_fk__in=cuentas_usuario) | Q(receptor_fk__in=cuentas_usuario))
    movimientos = movimientos.order_by('-fecha')

    movimientos_list = []

    for movimiento in movimientos:

        cuenta = movimiento.emisor_fk if movimiento.tipo_transaccion == 'DÉBITO' else movimiento.receptor_fk

        mov = {
            'fecha': movimiento.fecha,
            'referencia': movimiento.referencia,
            'descripcion': movimiento.descripcion,
            'tipo_transaccion': movimiento.tipo_transaccion,
            'monto': movimiento.monto,
            'saldo': movimiento.saldo_receptor if movimiento.tipo_transaccion == 'CRÉDITO' else movimiento.saldo_emisor,
            'numero_cuenta': cuenta.n_cuenta,
        }

        movimientos_list.append(mov)


    context = {'movimientos': movimientos_list,}

    return render(request, 'PerfilSolvenezApp/movimientos.html', context)
