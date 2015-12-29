# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_auto_20151119_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fecha_transaccion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
