# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0010_auto_20151116_1355'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='compra',
            unique_together=set([]),
        ),
    ]
