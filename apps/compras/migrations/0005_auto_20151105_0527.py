# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20151104_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='compra',
            name='razon_social',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='detalle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
