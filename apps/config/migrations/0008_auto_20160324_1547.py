# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_almacenescampos'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacenescampos',
            name='carac_especial_2_caractr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='carac_especial_2_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='carac_especial_2_tipo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='carac_especial_2_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='grupo_caractr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='grupo_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='grupo_tipo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='grupo_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='subgrupo_caractr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='subgrupo_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='subgrupo_tipo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='almacenescampos',
            name='subgrupo_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
