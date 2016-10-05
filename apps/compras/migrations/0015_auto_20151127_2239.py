# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_auto_20151127_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='nro_autorizacion',
            field=models.CharField(max_length=20),
        ),
    ]
