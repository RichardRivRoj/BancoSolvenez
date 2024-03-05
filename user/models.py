from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Estados(models.Model):

    estado = models.CharField(max_length=50)

class Municipios(models.Model):

    municipio = models.CharField(max_length=50)
    estado_fk = models.ForeignKey(Estados, null=False, blank=False ,on_delete=models.CASCADE)


class Zona(models.Model):
    
    zona = models.CharField(max_length=100)
    municipio_fk = models.ForeignKey(Municipios, null=False, blank=False ,on_delete=models.CASCADE)

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
    zonas = models.ManyToManyField(Zona, through='UsuarioZona')

class UsuarioZona(models.Model):
    usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)