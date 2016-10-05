# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20151105_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
