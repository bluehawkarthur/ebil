# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_auto_20151127_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='nro_autorizacion',
            field=models.IntegerField(),
        ),
    ]
