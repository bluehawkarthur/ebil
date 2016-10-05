# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('ventas', '0024_movimiento_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobro',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
