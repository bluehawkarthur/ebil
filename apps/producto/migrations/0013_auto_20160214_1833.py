# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('producto', '0012_item_fecha_transaccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
