# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0011_auto_20151116_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='descuento',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='excentos',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='ice',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='recargo',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
