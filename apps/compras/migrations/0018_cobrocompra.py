# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0017_auto_20151230_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='CobroCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_pago', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('fecha_transaccion', models.DateField(null=True, blank=True)),
                ('compra', models.ForeignKey(to='compras.Compra')),
            ],
        ),
    ]
