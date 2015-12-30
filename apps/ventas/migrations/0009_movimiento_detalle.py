# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_remove_movimiento_precio_unitario'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='detalle',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
    ]
