# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_personajuridica_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancarizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compra_fecha', models.DateField()),
                ('venta_fecha', models.DateField()),
                ('modal_transacc', models.CharField(max_length=100)),
                ('nro_d_cta_doc_de_pago', models.IntegerField()),
                ('fecha_fact_due_fec_doc', models.DateField()),
                ('monto_pagado_en_doc_d_pago', models.IntegerField()),
                ('tipo_transaccion', models.CharField(max_length=100)),
                ('monto_acumulado', models.IntegerField()),
                ('nro_d_fact_due_nro_doc', models.CharField(max_length=100)),
                ('nit_entidad_financiera', models.IntegerField()),
                ('monto_fact_monto_doc', models.IntegerField()),
                ('nro_d_docment_pago', models.IntegerField()),
                ('nro_d_autoriza_de_fect', models.IntegerField()),
                ('tipo_d_documet', models.CharField(max_length=100)),
                ('nit_ci_cliente', models.IntegerField()),
                ('fecha_d_document_pago', models.DateField()),
                ('razon_social_cliente', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(to='users.Personajuridica', null=True)),
            ],
        ),
    ]
