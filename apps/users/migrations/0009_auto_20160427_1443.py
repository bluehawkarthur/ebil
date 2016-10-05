# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono2',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono3',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
