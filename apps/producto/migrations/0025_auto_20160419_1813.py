# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0024_auto_20160418_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='carac_especial_1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='carac_especial_2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='grupo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='subgrupo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
