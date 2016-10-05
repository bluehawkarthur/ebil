# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0013_auto_20160214_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='proveedor',
            field=models.ForeignKey(related_name='proveedor', blank=True, to='proveedores.Proveedor', null=True),
        ),
    ]
