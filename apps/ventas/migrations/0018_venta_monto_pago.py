# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0017_auto_20160104_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='monto_pago',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
