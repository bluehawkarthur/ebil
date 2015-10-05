# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('razonSocial', models.CharField(max_length=50)),
                ('nit', models.IntegerField()),
                ('Direccion', models.CharField(max_length=50)),
                ('telefonos1', models.IntegerField()),
                ('telefonos2', models.IntegerField()),
                ('telefonos3', models.IntegerField()),
                ('contacto', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('UbucacionGeo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('fecha2', models.DateField()),
                ('textos', models.CharField(max_length=50)),
                ('textos2', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
