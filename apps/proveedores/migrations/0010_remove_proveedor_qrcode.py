# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0009_proveedor_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='qrcode',
        ),
    ]
