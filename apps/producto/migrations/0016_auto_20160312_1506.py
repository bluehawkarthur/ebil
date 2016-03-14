# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0015_auto_20160214_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='costo_unitario',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='precio_unitario',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
