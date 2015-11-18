# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('razonsocial', models.CharField(max_length=50)),
                ('nit', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('telefonos1', models.IntegerField()),
                ('telefonos2', models.IntegerField(null=True)),
                ('telefonos3', models.IntegerField(null=True)),
                ('contacto', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('ubucaciongeo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('fecha2', models.DateField()),
                ('textos', models.CharField(max_length=50)),
                ('textos2', models.CharField(max_length=50)),
            ],
        ),
    ]
