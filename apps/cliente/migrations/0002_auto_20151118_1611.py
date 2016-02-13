# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefonos1',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonos2',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonos3',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
