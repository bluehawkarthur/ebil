# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0004_proveedor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='texto1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='texto2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
