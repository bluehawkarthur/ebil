# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
        ('config', '0012_facturacampos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_sucursal', models.CharField(max_length=100)),
                ('nro_sucursal', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono1', models.IntegerField()),
                ('telefono2', models.IntegerField(null=True)),
                ('telefono3', models.IntegerField(null=True)),
                ('departamento', models.CharField(max_length=100)),
                ('municipios', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
    ]
