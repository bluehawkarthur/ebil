# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0017_auto_20160314_1516'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('codigo_item', 'codigo_fabrica', 'descripcion')]),
        ),
    ]
