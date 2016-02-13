# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='producto',
            field=models.ForeignKey(db_column=b'producto_id', blank=True, to='producto.Item', null=True),
        ),
    ]
