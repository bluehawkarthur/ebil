# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_auto_20151107_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='costo_unitario',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
    ]
