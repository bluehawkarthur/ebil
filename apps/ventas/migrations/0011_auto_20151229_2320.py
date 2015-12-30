# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_movimiento_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='precio_unitario',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
