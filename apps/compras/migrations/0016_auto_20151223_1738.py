# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0015_auto_20151127_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='descuento',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='excentos',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='ice',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='recargo',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_descuento',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_recargo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
