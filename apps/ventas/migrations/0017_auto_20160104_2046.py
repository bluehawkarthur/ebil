# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0016_venta_nro_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nro_factura',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
