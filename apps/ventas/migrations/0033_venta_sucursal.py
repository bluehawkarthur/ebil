# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0013_sucursal'),
        ('ventas', '0032_cobro_nro'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='config.Sucursal', null=True),
        ),
    ]
