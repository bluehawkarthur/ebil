# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160214_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosDosificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_conrelativo', models.BigIntegerField()),
                ('fecha', models.DateField()),
                ('nro_autorizacion', models.BigIntegerField()),
                ('llave_digital', models.CharField(max_length=200)),
                ('empresa', models.ForeignKey(blank=True, to='users.Personajuridica', null=True)),
            ],
        ),
    ]
