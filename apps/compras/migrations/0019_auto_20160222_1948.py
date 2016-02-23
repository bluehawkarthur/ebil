# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_compra_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.BigIntegerField(),
        ),
    ]
