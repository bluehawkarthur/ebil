# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0016_auto_20151223_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='nit',
            field=models.BigIntegerField(),
        ),
    ]
