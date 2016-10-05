# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0030_auto_20160317_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobro',
            name='monto_pago',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
