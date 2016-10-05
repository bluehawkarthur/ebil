# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0014_movimiento_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nit',
            field=models.BigIntegerField(),
        ),
    ]
