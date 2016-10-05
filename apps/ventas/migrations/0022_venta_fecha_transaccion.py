# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0021_remove_venta_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_transaccion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
