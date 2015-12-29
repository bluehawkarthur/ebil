# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20151117_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='descuento',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='excentos',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='ice',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='recargo',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='tipo_descuento',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='tipo_recargo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
