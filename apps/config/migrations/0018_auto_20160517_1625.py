# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0017_auto_20160517_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='formatofactura',
            name='facturacion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formatofactura',
            name='frases_pie',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formatofactura',
            name='frases_subtitulo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formatofactura',
            name='frases_titulo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formatofactura',
            name='impresion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formatofactura',
            name='tamanio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
