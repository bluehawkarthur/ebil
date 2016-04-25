# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0016_auto_20160312_1506'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([]),
        ),
    ]
