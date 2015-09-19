# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='proveedor',
            field=models.ForeignKey(related_name='proveedor', to='proveedores.Proveedor'),
        ),
    ]
