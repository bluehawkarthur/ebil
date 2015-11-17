# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20151116_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='descuento',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='excentos',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='ice',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='recargo',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
