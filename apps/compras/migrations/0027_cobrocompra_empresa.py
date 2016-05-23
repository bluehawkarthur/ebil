# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160427_1443'),
        ('compras', '0026_compra_nro_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobrocompra',
            name='empresa',
            field=models.ForeignKey(blank=True, to='users.Personajuridica', null=True),
        ),
    ]
