# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0036_auto_20160427_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='precio_unitario',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
