# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20160325_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='categoria',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contacto',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha2',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rubro',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonos1',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonos2',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonos3',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='textos',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='textos2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ubucaciongeo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
