# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0022_auto_20160314_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='codigo_fabrica',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
