# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('proveedores', '0005_auto_20150925_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='user',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
