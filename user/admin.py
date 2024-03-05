from django.contrib import admin
from .models import User, UsuarioZona ,Zona, Municipios, Estados

# Register your models here.
admin.site.register(User)
admin.site.register(UsuarioZona)
admin.site.register(Zona)
admin.site.register(Municipios)
admin.site.register(Estados)