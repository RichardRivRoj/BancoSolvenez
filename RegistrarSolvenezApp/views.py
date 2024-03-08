from django.shortcuts import render, redirect
from user.models import User, Cuenta
from .forms import CustomUserCreationForm, ValidarForm, VerificacionFrom
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
import random

# Create your views here.

def validar(request):

    if request.method == 'POST':

        formV = ValidarForm(request.POST)

        if formV.is_valid():

            tipo_doc = formV.cleaned_data['tipo_doc']
            cedula = formV.cleaned_data['cedula']

            if User.objects.filter(tipo_doc=tipo_doc, cedula=cedula).exists():
                return redirect('validar')
            else:
                return redirect('terminos')
    else:
        formV = ValidarForm()

    return render(request, 'RegistrarSolvenezApp/validar.html', {'formV':formV})

def terminos(request):



    return render(request, 'RegistrarSolvenezApp/terminos.html')

def registro(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            codigo_verificacion = get_random_string(6) 

            correo_usuario = request.POST.get('email')

            remitente = settings.EMAIL_HOST_USER
            asunto = 'Código de verificación'
            mensaje = f'Su código de verificación es: {codigo_verificacion}'

            # Envío del código de verificación por cortreo electrónico

            send_mail(
                asunto,
                mensaje,
                remitente,
                [correo_usuario],
                fail_silently=False,
            )

            request.session['codigo_verificacion'] = codigo_verificacion
            request.session['datos_registro'] = request.POST.dict()

            return redirect('email')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

def email(request):

    if request.method == 'POST':

        formE = VerificacionFrom(request.POST)

        if formE.is_valid():

            codigo_ingresado = formE.cleaned_data['codigo']
            codigo_verificacion = request.session.get('codigo_verificacion')

            if codigo_ingresado == str(codigo_verificacion):

                datos_registro = request.session.get('datos_registro')

                # Guardar en la Base de Datos

                user_creacion = User.objects.create(
                    first_name = datos_registro['first_name'],
                    last_name = datos_registro['last_name'],
                    tipo_doc = datos_registro['tipo_doc'],
                    cedula = datos_registro['cedula'],
                    fecha_nacimiento = datos_registro['fecha_nacimiento'],
                    genero = datos_registro['genero'],
                    username = datos_registro['username'],
                    email = datos_registro['email'],
                    pregunta_seguridad = datos_registro['pregunta_seguridad'], 
                    respuesta_seguridad = datos_registro['respuesta_seguridad'], 
                    password = make_password(datos_registro['password1']),    
                )

                user_creacion.save()
                user = authenticate(username=datos_registro['username'], password=datos_registro['password1'])

                del request.session['codigo_verificacion']
                del request.session['datos_registro']

                if user is not None:
                    login(request, user)
                    return redirect('datos_registro')
            else:
                mensaje_error = 'Código incorrecto, ¿Intenta de nuevo?'
                return render(request, 'RegistrarSolvenezApp/email.html', {'formE': formE, 'error': mensaje_error})
    else:
        formE = VerificacionFrom()

    return render(request, 'RegistrarSolvenezApp/email.html', {'formE': formE})

def datos_registro(request):

    cuenta = Cuenta.objects.filter(user_fk=request.user).first()

    return render(request, 'RegistrarSolvenezApp/datos_registro.html', {'usuario': request.user, 'cuenta': cuenta})
