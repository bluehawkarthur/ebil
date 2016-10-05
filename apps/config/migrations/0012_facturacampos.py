# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
        ('config', '0011_auto_20160329_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCampos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuento_usar', models.BooleanField()),
                ('descuento_requerido', models.BooleanField()),
                ('recargo_usar', models.BooleanField()),
                ('recargo_requerido', models.BooleanField()),
                ('ice_usar', models.BooleanField()),
                ('ice_requerido', models.BooleanField()),
                ('exentos_usar', models.BooleanField()),
                ('exentos_requerido', models.BooleanField()),
                ('tipos_venta_usar', models.BooleanField()),
                ('tipos_venta_requerido', models.BooleanField()),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
    ]
