# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='telefono2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono3',
            field=models.IntegerField(null=True),
        ),
    ]
