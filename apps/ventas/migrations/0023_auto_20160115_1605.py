# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0022_venta_fecha_transaccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_pago', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('fecha_transaccion', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='venta',
            name='fecha_transaccion',
        ),
        migrations.AddField(
            model_name='cobro',
            name='venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
