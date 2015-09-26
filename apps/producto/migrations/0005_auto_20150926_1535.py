# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20150925_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagen',
            field=models.ImageField(default='sssss', upload_to=b'items'),
            preserve_default=False,
        ),
    ]
