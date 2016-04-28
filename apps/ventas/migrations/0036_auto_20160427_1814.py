# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0035_venta_nro_baja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nit',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
