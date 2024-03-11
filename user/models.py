from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    tipos_doc = {
        'V': 'Venezolano',
        'E': 'Extranjero',
        'P': 'Pasaporte',
    }

    generos = {
        'M' : 'Masculino',
        'F' : 'Femenino',
        'I' : 'Indefinido',
    }

    tipo_doc = models.CharField(max_length=1, choices=tipos_doc)
    cedula = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True)
    genero = models.CharField(max_length=1, choices=generos)
    telefono = models.CharField(max_length=15)
    pregunta_seguridad = models.TextField(max_length=100)
    respuesta_seguridad = models.TextField(max_length=100)

class Cuenta(models.Model):

    TIPO_CUENTA_CHOICES = (
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorros'),
    )

    n_cuenta = models.CharField(max_length=20)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA_CHOICES, default='corriente')
    saldo = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.n_cuenta} - {self.tipo_cuenta}"