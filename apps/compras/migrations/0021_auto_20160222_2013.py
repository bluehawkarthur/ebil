# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0020_auto_20160222_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='scf',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotal',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
