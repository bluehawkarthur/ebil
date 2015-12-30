# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_movimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='precio_unitario',
        ),
    ]
