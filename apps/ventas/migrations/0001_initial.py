# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20151105_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('descuento', models.IntegerField(default=0)),
                ('recargo', models.IntegerField(default=0)),
                ('ice', models.IntegerField()),
                ('excentos', models.IntegerField()),
                ('scf', models.DecimalField(max_digits=6, decimal_places=2)),
                ('item', models.ForeignKey(to='producto.Item', db_column=b'producto_id')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('nit', models.IntegerField()),
                ('razon_social', models.CharField(max_length=100)),
                ('tipo_compra', models.CharField(max_length=100)),
                ('cantidad_dias', models.IntegerField()),
                ('total', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='venta',
            unique_together=set([('nit',)]),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
