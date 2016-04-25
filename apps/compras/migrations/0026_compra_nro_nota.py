# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0025_auto_20160311_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='nro_nota',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
