# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160213_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='empresa',
            field=models.ForeignKey(to='users.Personajuridica', null=True),
        ),
    ]
