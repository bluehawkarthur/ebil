# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_auto_20160214_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]
