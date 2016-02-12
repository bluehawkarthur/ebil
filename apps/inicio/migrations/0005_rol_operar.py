# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_auto_20160211_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='operar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
