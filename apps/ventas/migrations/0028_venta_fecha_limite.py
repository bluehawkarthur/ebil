# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0027_auto_20160229_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_limite',
            field=models.DateField(null=True, blank=True),
        ),
    ]
