# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_auto_20160419_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formatodetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('impresion', models.CharField(max_length=100)),
                ('facturacion', models.CharField(max_length=100)),
                ('tamanio', models.CharField(max_length=100)),
                ('frases_titulo', models.CharField(max_length=100)),
                ('frases_subtitulo', models.CharField(max_length=100)),
                ('frases_pie', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='facturacion',
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='frases_pie',
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='frases_subtitulo',
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='frases_titulo',
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='impresion',
        ),
        migrations.RemoveField(
            model_name='formatofactura',
            name='tamanio',
        ),
        migrations.AddField(
            model_name='formatodetalle',
            name='formatofact',
            field=models.ForeignKey(blank=True, to='config.Formatofactura', null=True),
        ),
        migrations.AddField(
            model_name='formatodetalle',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='config.Sucursal', null=True),
        ),
    ]
