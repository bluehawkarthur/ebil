# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20151118_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.BigIntegerField(),
        ),
    ]
