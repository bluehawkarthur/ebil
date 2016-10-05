# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
        ('config', '0009_auto_20160324_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProveedoresCampos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion_usar', models.BooleanField()),
                ('direccion_requerido', models.BooleanField()),
                ('direccion_tipo', models.CharField(max_length=100)),
                ('direccion_caractr', models.IntegerField()),
                ('telefonos1_usar', models.BooleanField()),
                ('telefonos1_requerido', models.BooleanField()),
                ('telefonos1_tipo', models.CharField(max_length=100)),
                ('telefonos1_caractr', models.IntegerField()),
                ('telefonos2_usar', models.BooleanField()),
                ('telefonos2_requerido', models.BooleanField()),
                ('telefonos2_tipo', models.CharField(max_length=100)),
                ('telefonos2_caractr', models.IntegerField()),
                ('telefonos3_usar', models.BooleanField()),
                ('telefonos3_requerido', models.BooleanField()),
                ('telefonos3_tipo', models.CharField(max_length=100)),
                ('telefonos3_caractr', models.IntegerField()),
                ('contacto_usar', models.BooleanField()),
                ('contacto_requerido', models.BooleanField()),
                ('contacto_tipo', models.CharField(max_length=100)),
                ('contacto_caractr', models.IntegerField()),
                ('rubro_usar', models.BooleanField()),
                ('rubro_requerido', models.BooleanField()),
                ('rubro_tipo', models.CharField(max_length=100)),
                ('rubro_caractr', models.IntegerField()),
                ('ubicacion_geo_usar', models.BooleanField()),
                ('ubicacion_geo_requerido', models.BooleanField()),
                ('ubicacion_geo_tipo', models.CharField(max_length=100)),
                ('ubicacion_geo_caractr', models.IntegerField()),
                ('fechas_usar', models.BooleanField()),
                ('fechas_requerido', models.BooleanField()),
                ('fechas2_usar', models.BooleanField()),
                ('fechas2_requerido', models.BooleanField()),
                ('textos_usar', models.BooleanField()),
                ('textos_requerido', models.BooleanField()),
                ('textos_tipo', models.CharField(max_length=100)),
                ('textos_caractr', models.IntegerField()),
                ('textos2_usar', models.BooleanField()),
                ('textos2_requerido', models.BooleanField()),
                ('textos2_tipo', models.CharField(max_length=100)),
                ('textos2_caractr', models.IntegerField()),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
    ]
