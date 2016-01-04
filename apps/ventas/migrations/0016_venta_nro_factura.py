# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0015_auto_20151230_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='nro_factura',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
