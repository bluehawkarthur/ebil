# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0006_auto_20160214_1856'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='proveedor',
            unique_together=set([('codigo', 'empresa')]),
        ),
    ]
