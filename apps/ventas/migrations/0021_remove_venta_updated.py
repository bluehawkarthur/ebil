# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0020_venta_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='updated',
        ),
    ]
