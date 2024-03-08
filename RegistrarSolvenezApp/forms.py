from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'tipo_doc',
            'cedula',
            'fecha_nacimiento',
            'genero',
            'username',
            'email',
            'pregunta_seguridad',
            'respuesta_seguridad',
            'password1',
            'password2',
            ]
         

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Nombres', 'class':'form0', 'id':'Nombres', 'required': 'required',
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Apellidos', 'class':'form0', 'id':'Apellidos', 'required': 'required',
            }),

            'tipo_doc': forms.Select(attrs={
                'placeholder': 'Tipo de Documento', 'class':'form0', 'id':'Tipo_docu', 'required': 'required',
            }),

            'cedula': forms.TextInput(attrs={
                'placeholder': 'N° Documento', 'class':'form0', 'id':'cedula', 'required': 'required',
            }),

            'fecha_nacimiento': forms.DateInput(attrs={
                'placeholder': 'Fecha de Nacimiento', 'class':'form0', 'id':'Fecha_nac', 'required': 'required',
            }),

            'genero': forms.Select(attrs={
                'placeholder': 'Género', 'class':'form0', 'id':'genero', 'required': 'required',
            }),

            'username': forms.TextInput(attrs={
                'placeholder': 'Usuario', 'class':'form0', 'id':'usuario', 'required': 'required',
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Correo Electrónico', 'class':'form0', 'id':'Email', 'required': 'required',
            }),

            'pregunta_seguridad': forms.TextInput(attrs={
                'placeholder': 'Pregunta de Seguridad', 'class':'form0', 'id':'PreSegurity', 'required': 'required',
            }),

            'respuesta_seguridad': forms.TextInput(attrs={
                'placeholder': 'Respuesta de Seguridad', 'class':'form0', 'id':'ResSegurity', 'required': 'required',
            }),

            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Clave de acceso', 'class':'form0', 'id':'password_1', 'required': 'required',
            }),

            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirmar Clave de acceso', 'class':'form0', 'id':'password_2', 'required': 'required',
            }),
        }

        labels = {
            'first_name':'',
            'last_name':'',
            'tipo_doc':'',
            'cedula':'',
            'fecha_nacimiento':'',
            'genero':'',
            'email':'',
            'pregunta_seguridad':'',
            'respuesta_seguridad':'',
            'password1':'',
            'password2':'',
        }
    
class ValidarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'tipo_doc',
            'cedula',
        ]

        widgets = {

            'tipo_doc': forms.Select(attrs={
                'placeholder': 'Tipo de Documento', 'class':'Tipo_doc', 'id':'form0', 'required': 'required',
            }),

            'cedula': forms.TextInput(attrs={
                'placeholder': 'N° Documento', 'class':'documento', 'id':'form0', 'required': 'required',
            }),
        }

        labels = {
            'tipo_doc':'',
            'cedula':'',
        }


class VerificacionFrom(forms.Form):

    codigo = forms.CharField(
        label= '*Código de confirmación:',
        widget= forms.TextInput(attrs={
            'placeholder': 'Introduzca el código', 'class':'codigo', 'id':'form0', 'required': 'required',
        })
    )
