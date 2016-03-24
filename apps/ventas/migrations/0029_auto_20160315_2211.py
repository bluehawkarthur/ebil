# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0028_venta_fecha_limite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='codigo_control',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='llave_digital',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_autorizacion',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
