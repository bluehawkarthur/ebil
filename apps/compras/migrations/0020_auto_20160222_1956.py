# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0019_auto_20160222_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='scf',
            field=models.BigIntegerField(),
        ),
    ]
