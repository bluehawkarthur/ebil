# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_cobrocompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fecha_vencimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='monto_pago',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
