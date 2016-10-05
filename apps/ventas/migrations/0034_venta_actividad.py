# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0033_venta_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='actividad',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
