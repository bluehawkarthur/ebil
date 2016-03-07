# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_clientecampos'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientecampos',
            name='nit_caractr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='nit_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='nit_tipo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='nit_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
