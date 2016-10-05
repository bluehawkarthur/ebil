# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancarizacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bancarizacion',
            old_name='nit_ci_cliente',
            new_name='nit_proveedor',
        ),
        migrations.RenameField(
            model_name='bancarizacion',
            old_name='razon_social_cliente',
            new_name='razon_social_proveedor',
        ),
    ]
