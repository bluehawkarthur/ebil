# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0029_auto_20160315_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='nro_nota',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='tipo_movimiento',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
