# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
        ('config', '0002_datosdosificacion_contador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formatofactura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('formato', models.CharField(max_length=100)),
                ('impresion', models.CharField(max_length=100)),
                ('facturacion', models.CharField(max_length=100)),
                ('tamanio', models.CharField(max_length=100)),
                ('frases_titulo', models.CharField(max_length=100)),
                ('frases_subtitulo', models.CharField(max_length=100)),
                ('frases_pie', models.CharField(max_length=200)),
                ('Personajuridica', models.ForeignKey(blank=True, to='users.Personajuridica', null=True)),
            ],
        ),
    ]
