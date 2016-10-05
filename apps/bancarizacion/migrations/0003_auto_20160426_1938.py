# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
        ('bancarizacion', '0002_auto_20160420_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancarizacionCompras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compra_fecha', models.DateField()),
                ('modalidad_d_la_transaccion', models.CharField(max_length=100)),
                ('nro_de_cta_doc_de_pago', models.IntegerField()),
                ('fecha_fact_dui_fecha_doc', models.DateField()),
                ('monto_pagado_en_doc_d_pago', models.IntegerField()),
                ('tipo_transaccion', models.CharField(max_length=100)),
                ('monto_acumulado', models.IntegerField()),
                ('nit_proveedor', models.IntegerField()),
                ('nit_entidad_inanciera', models.IntegerField()),
                ('razon_social_proveedor', models.CharField(max_length=100)),
                ('nro_d_documento_de_pago', models.IntegerField()),
                ('nro_d_fact_dui_nro_doc', models.IntegerField()),
                ('tipo_de_doc_d_pago', models.CharField(max_length=100)),
                ('tipo_de_documento', models.CharField(max_length=100)),
                ('monto_fact_monto_dui_monto_doc', models.CharField(max_length=100)),
                ('fecha_d_documento_d_pago', models.DateField()),
                ('nro_de_aut_fact_dui_documento', models.IntegerField()),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BancarizacionVentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venta_fecha', models.DateField()),
                ('modalidad_d_la_transaccion', models.CharField(max_length=100)),
                ('nro_de_cta_doc_de_pago', models.IntegerField()),
                ('fecha_fact_dui_fecha_doc', models.DateField()),
                ('monto_pagado_en_doc_d_pago', models.IntegerField()),
                ('tipo_transaccion', models.CharField(max_length=100)),
                ('monto_acumulado', models.IntegerField()),
                ('nro_d_fact_dui_nro_doc', models.IntegerField()),
                ('nit_entidad_inanciera', models.IntegerField()),
                ('monto_fact_monto_doc', models.CharField(max_length=100)),
                ('nro_d_documento_de_pago', models.IntegerField()),
                ('nro_de_auturizacion_d_fact', models.IntegerField()),
                ('tipo_de_doc_d_pago', models.CharField(max_length=100)),
                ('tipo_de_documento', models.CharField(max_length=100)),
                ('nit_ci_d_cliente', models.IntegerField()),
                ('fecha_d_documento_d_pago', models.DateField()),
                ('razon_social_cliente', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bancarizacion',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='Bancarizacion',
        ),
    ]
