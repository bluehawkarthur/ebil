# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_item', models.CharField(max_length=10)),
                ('codigo_fabrica', models.CharField(max_length=10)),
                ('almacen', models.IntegerField()),
                ('grupo', models.CharField(max_length=50)),
                ('subgrupo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('carac_especial_1', models.CharField(max_length=50)),
                ('carac_especial_2', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('saldo_min', models.IntegerField()),
                ('imagen', models.ImageField(upload_to=b'items')),
                ('unidad_medida', models.CharField(max_length=20)),
                ('costo_unitario', models.DecimalField(max_digits=5, decimal_places=3)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
