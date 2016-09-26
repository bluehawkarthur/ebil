# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0008_auto_20160214_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='qrcode',
            field=models.ImageField(null=True, upload_to=b'qrcode', blank=True),
        ),
    ]
