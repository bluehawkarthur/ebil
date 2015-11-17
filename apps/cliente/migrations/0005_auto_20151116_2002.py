# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20151116_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='razonSocial',
            new_name='razoncocial',
        ),
    ]
