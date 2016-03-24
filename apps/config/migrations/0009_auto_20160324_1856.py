# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20160324_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almacenescampos',
            name='codigo_itemcaractr',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='codigo_itemtipo',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='codigo_requerido',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='codigo_usar',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='descrip_caractr',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='descrip_requerido',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='descrip_tipo',
        ),
        migrations.RemoveField(
            model_name='almacenescampos',
            name='descrip_usar',
        ),
    ]
