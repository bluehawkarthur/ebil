# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_auto_20151117_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='nro_autorizacion',
            field=models.BigIntegerField(max_length=20),
        ),
    ]
