# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20160211_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='editar',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='rol',
            name='eliminar',
            field=models.NullBooleanField(),
        ),
    ]
