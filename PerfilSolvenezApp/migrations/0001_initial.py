# Generated by Django 5.0.2 on 2024-03-10 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0006_remove_municipios_estado_fk_remove_zona_municipio_fk_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='movimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('referencia', models.CharField(max_length=13)),
                ('descripcion', models.CharField(choices=[('PAGO MÓVIL', 'Pago móvil'), ('TRANSFERENCIAS A TERCEROS', 'Transferencias a terceros'), ('TRANSFERENCIAS A OTROS BANCOS NACIONALES', 'Transferencias a otros bancos nacionales'), ('RECARGAS', 'Recargas'), ('PAGO DE NÓMINA', 'Pago de nómina'), ('COMPRA CON TARJETA DE DÉBITO', 'Compra con tarjeta de débito')], max_length=50)),
                ('tipo_transaccion', models.CharField(choices=[('DÉBITO', 'Débito'), ('CRÉDITO', 'Crédito')], max_length=10)),
                ('monto', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('emisor_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacciones_emitidas', to='user.cuenta')),
                ('receptor_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacciones_recibidas', to='user.cuenta')),
            ],
        ),
    ]
