# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('config', '0004_auto_20160225_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteCampos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_usar', models.BooleanField()),
                ('codigo_requerido', models.BooleanField()),
                ('codigo_tipo', models.CharField(max_length=100)),
                ('codigo_caractr', models.IntegerField()),
                ('razonsocal_usar', models.BooleanField()),
                ('razonsocal_requerido', models.BooleanField()),
                ('razonsocal_tipo', models.CharField(max_length=100)),
                ('razonsocal_caractr', models.IntegerField()),
                ('direccion_usar', models.BooleanField()),
                ('direccion_requerido', models.BooleanField()),
                ('direccion_tipo', models.CharField(max_length=100)),
                ('direccion_caractr', models.IntegerField()),
                ('telefonos_usar', models.BooleanField()),
                ('telefonos_requerido', models.BooleanField()),
                ('telefonos_tipo', models.CharField(max_length=100)),
                ('telefonos_caractr', models.IntegerField()),
                ('contacto_usar', models.BooleanField()),
                ('contacto_requerido', models.BooleanField()),
                ('contacto_tipo', models.CharField(max_length=100)),
                ('contacto_caractr', models.IntegerField()),
                ('rubro_usar', models.BooleanField()),
                ('rubro_requerido', models.BooleanField()),
                ('rubro_tipo', models.CharField(max_length=100)),
                ('rubro_caractr', models.IntegerField()),
                ('ubicaciongeo_usar', models.BooleanField()),
                ('ubicaciongeo_requerido', models.BooleanField()),
                ('ubicaciongeo_tipo', models.CharField(max_length=100)),
                ('ubicaciongeo_caractr', models.IntegerField()),
                ('categoria_usar', models.BooleanField()),
                ('categoria_requerido', models.BooleanField()),
                ('categoria_tipo', models.CharField(max_length=100)),
                ('categoria_caractr', models.IntegerField()),
                ('empresa', models.ForeignKey(blank=True, to='users.Personajuridica', null=True)),
            ],
        ),
    ]
