# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='personajuridica',
            name='logo',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'logo', blank=True),
        ),
    ]
