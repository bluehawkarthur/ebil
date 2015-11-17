# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20151104_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecompra',
            old_name='precio',
            new_name='precio_unitario',
        ),
        migrations.RenameField(
            model_name='detallecompra',
            old_name='cf',
            new_name='scf',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='excentos',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='ice',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='monto',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='recargo',
        ),
    ]
