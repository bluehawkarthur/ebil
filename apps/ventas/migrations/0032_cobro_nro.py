# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0031_auto_20160318_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobro',
            name='nro',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
