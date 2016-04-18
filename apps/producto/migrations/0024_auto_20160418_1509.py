# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0023_auto_20160324_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='codigo_item',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
