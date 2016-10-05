# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20150923_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
