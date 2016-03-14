# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0022_auto_20160222_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroCostos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100, null=True, blank=True)),
                ('cod', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
