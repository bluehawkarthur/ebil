# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20150926_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'items'),
        ),
    ]
