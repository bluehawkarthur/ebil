# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_empresa'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together=set([('codigo', 'nit')]),
        ),
    ]
