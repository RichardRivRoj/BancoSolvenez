from django.db import models
from user.models import User, Cuenta

# Create your models here.

class Movimientos(models.Model):

    TIPO_TRANSACCION = (
        ('DÉBITO', 'Débito'),
        ('CRÉDITO', 'Crédito'),
    )

    DESCRIPCION = (
        ('PAGO MÓVIL', 'Pago móvil'),
        ('TRANSFERENCIAS A TERCEROS', 'Transferencias a terceros'),
        ('TRANSFERENCIAS A OTROS BANCOS NACIONALES', 'Transferencias a otros bancos nacionales'),
        ('RECARGAS', 'Recargas'),
        ('PAGO DE NÓMINA', 'Pago de nómina'),
        ('COMPRA CON TARJETA DE DÉBITO', 'Compra con tarjeta de débito'),
    )

    fecha = models.DateTimeField(null=True, auto_now_add=True)
    referencia = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=50, choices=DESCRIPCION, default='TRANSFERENCIAS A TERCEROS')
    tipo_transaccion = models.CharField(max_length=10, choices=TIPO_TRANSACCION)
    monto = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    saldo_receptor = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    saldo_emisor = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    emisor_fk = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transacciones_emitidas')
    receptor_fk = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transacciones_recibidas')

    def __str__(self):

        return self.emisor_fk

