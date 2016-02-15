# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160214_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono3',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
