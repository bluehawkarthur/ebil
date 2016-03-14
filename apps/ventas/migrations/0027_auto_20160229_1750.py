# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0026_auto_20160224_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='codigo_control',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='llave_digital',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='numero_autorizacion',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
