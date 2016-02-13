# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20150926_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.IntegerField()),
                ('razon_social', models.CharField(max_length=6)),
                ('nro_factura', models.IntegerField()),
                ('nro_autorizacion', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('monto', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('recargo', models.IntegerField()),
                ('ice', models.IntegerField()),
                ('excentos', models.IntegerField()),
                ('cod_control', models.CharField(max_length=100)),
                ('total', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=10)),
                ('detalle', models.CharField(max_length=40)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('descuento', models.IntegerField()),
                ('recargo', models.IntegerField()),
                ('ice', models.IntegerField()),
                ('excentos', models.IntegerField()),
                ('cf', models.IntegerField()),
                ('centro_costos', models.CharField(max_length=100)),
                ('compra', models.ForeignKey(to='compras.Compra', db_column=b'compra_id')),
                ('producto', models.ForeignKey(to='producto.Item', db_column=b'producto_id')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='compra',
            unique_together=set([('nit', 'nro_factura')]),
        ),
    ]
