# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
        ('config', '0006_auto_20160307_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlmacenesCampos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_usar', models.BooleanField()),
                ('codigo_requerido', models.BooleanField()),
                ('codigo_itemtipo', models.CharField(max_length=100)),
                ('codigo_itemcaractr', models.IntegerField()),
                ('codigo_fabr_usar', models.BooleanField()),
                ('codigo_fabr_reque', models.BooleanField()),
                ('codigo_fabricatipo', models.CharField(max_length=100)),
                ('codigo_fabricacaractr', models.IntegerField()),
                ('descrip_usar', models.BooleanField()),
                ('descrip_requerido', models.BooleanField()),
                ('descrip_tipo', models.CharField(max_length=100)),
                ('descrip_caractr', models.IntegerField()),
                ('caract_espec_usar', models.BooleanField()),
                ('caract_espec_requerid', models.BooleanField()),
                ('caract_espectipo', models.CharField(max_length=100)),
                ('caract_especaractr', models.IntegerField()),
                ('unidad_medid_usar', models.BooleanField()),
                ('unidad_medid_requerido', models.BooleanField()),
                ('unidad_medidatipo', models.CharField(max_length=100)),
                ('unidad_medidacaractr', models.IntegerField()),
                ('imagen_usar', models.BooleanField()),
                ('imagen_requer', models.BooleanField()),
                ('empresa', models.ForeignKey(blank=True, to='users.Personajuridica', null=True)),
            ],
        ),
    ]
