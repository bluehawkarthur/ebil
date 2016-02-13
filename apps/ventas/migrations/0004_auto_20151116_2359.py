# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20151116_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='tipo_descuento',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='tipo_recargo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
