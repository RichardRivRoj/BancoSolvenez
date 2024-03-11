from django import forms
from .models import Movimientos

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        fields = [
            'emisor_fk',
            'receptor_fk',
            'monto',
        ]

        widgets = {

            'emisor_fk': forms.Select(attrs={
                'placeholder': 'Cuenta a debitar', 'class':'emisor', 'id':'form0', 'required': 'required',
            }),

            'receptor_fk': forms.Select(attrs={
                'placeholder': 'Cuenta destino', 'class':'receptor', 'id':'form0', 'required': 'required',
            }),

            'monto': forms.NumberInput(attrs={
                'placeholder': 'Monto', 'class':'monto', 'id':'form0', 'required': 'required',
            }),
        }

        labels = {
            'emisor_fk':'Cuenta a debitar:',
            'receptor_fk':'Cuenta destino:',
            'monto':'Monto:',
        }