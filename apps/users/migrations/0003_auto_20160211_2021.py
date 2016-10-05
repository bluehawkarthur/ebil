# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160202_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'users'),
        ),
    ]
