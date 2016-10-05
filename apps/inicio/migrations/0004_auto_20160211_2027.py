# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20160211_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='editar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rol',
            name='eliminar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
