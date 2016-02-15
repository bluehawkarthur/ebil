# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160213_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='empresa',
        ),
    ]
