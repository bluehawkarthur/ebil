# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_formatofactura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formatofactura',
            old_name='Personajuridica',
            new_name='empresa',
        ),
    ]
