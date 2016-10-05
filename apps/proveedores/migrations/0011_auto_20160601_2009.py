# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0010_remove_proveedor_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='telefono1',
            field=models.IntegerField(null=True),
        ),
    ]
