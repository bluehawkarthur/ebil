# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20151116_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='razoncocial',
            new_name='razonsocial',
        ),
    ]
