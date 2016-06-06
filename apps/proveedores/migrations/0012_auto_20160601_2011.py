# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0011_auto_20160601_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha2',
            field=models.DateField(null=True),
        ),
    ]
