# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_movimiento_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='precio_unitario',
            field=models.DecimalField(default=(89), max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
