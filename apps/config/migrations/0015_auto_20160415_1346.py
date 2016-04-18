# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0014_actividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosdosificacion',
            name='actividad',
            field=models.ForeignKey(blank=True, to='config.Actividad', null=True),
        ),
        migrations.AddField(
            model_name='datosdosificacion',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='config.Sucursal', null=True),
        ),
    ]
