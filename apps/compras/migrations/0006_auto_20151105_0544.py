# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20151105_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotal',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
