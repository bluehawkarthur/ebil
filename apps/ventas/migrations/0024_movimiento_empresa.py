# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('ventas', '0023_auto_20160115_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
