# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20150818_2254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Libro',
        ),
    ]
