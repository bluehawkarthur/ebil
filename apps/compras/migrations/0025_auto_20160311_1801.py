# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0024_centrocostos_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='CobroCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_pago', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('fecha_transaccion', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_vencimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='monto_pago',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='cobrocompra',
            name='compra',
            field=models.ForeignKey(to='compras.Compra'),
        ),
    ]
