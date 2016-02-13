# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20151105_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='tipo_descuento',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='tipo_recargo',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
