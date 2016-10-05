# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20151105_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='carac_especial_1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='carac_especial_2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='codigo_fabrica',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='codigo_item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='grupo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='subgrupo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='unidad_medida',
            field=models.CharField(max_length=100),
        ),
    ]
