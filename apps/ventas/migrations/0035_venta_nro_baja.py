# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0034_venta_actividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='nro_baja',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
