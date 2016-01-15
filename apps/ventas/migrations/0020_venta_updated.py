# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0019_venta_fecha_vencimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 22, 51, 16, 628247, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
