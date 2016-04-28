# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0025_auto_20160419_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='codigo_item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('codigo_item', 'empresa')]),
        ),
    ]
