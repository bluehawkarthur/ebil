# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0005_auto_20150925_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='user',
        ),
    ]
