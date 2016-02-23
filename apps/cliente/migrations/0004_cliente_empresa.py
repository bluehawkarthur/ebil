# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('cliente', '0003_auto_20151207_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
