# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cliente_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='UbucacionGeo',
            new_name='ubucaciongeo',
        ),
    ]
