# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20151104_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cantidad_dias',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_compra',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
