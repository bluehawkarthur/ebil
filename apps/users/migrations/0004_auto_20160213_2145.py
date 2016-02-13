# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160211_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personajuridica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('nit', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('telefono2', models.IntegerField()),
                ('telefono3', models.IntegerField()),
                ('departamento', models.CharField(max_length=100)),
                ('municipios', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(null=True, to='users.Personajuridica'),
        ),
    ]
