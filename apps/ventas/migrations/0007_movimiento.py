# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0012_item_fecha_transaccion'),
        ('ventas', '0006_auto_20151226_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(max_digits=6, decimal_places=2)),
                ('fecha_transaccion', models.DateField()),
                ('motivo_movimiento', models.CharField(max_length=100)),
                ('item', models.ForeignKey(to='producto.Item', db_column=b'producto_id')),
            ],
        ),
    ]
