# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0018_venta_monto_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_vencimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
