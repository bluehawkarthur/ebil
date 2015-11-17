# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20150926_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='costo_unitario',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='precio_unitario',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
