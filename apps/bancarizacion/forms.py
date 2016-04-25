# -*- coding: utf-8 -*-
from django import forms, http
from .models import Bancarizacion
from django.forms import ModelForm
# Create your models here.

class BancarizacionForm(forms.Form):
	compra_fecha = forms.DateField()
	venta_fecha = forms.DateField()
	modal_transacc = forms.CharField(max_length=100, label='Modalidad de  la transacción')
	nro_d_cta_doc_de_pago = forms.IntegerField(label='Nro. De Cta. Doc. de pago')
	fecha_fact_due_fec_doc = forms.DateField(label='Fecha fact. DUI/Fecha Doc.')
	monto_pagado_en_doc_d_pago = forms.IntegerField(label='Monto pagado en Doc. De pago')
	tipo_transaccion = forms.CharField(max_length=100)
	monto_acumulado = forms.IntegerField()
	nro_d_fact_due_nro_doc = forms.CharField(max_length=100, label='Nro. De fact. DUI/Nro. Doc.')
	nit_entidad_financiera = forms.IntegerField(label='NIT Entidad Financiera')
	monto_fact_monto_doc = forms.IntegerField(label='Monto fact./Monto DUI/Monto Doc')
	nro_d_docment_pago = forms.CharField(max_length=100, label='Nro. de Documento de pago')
	nro_d_autoriza_de_fect = forms.IntegerField(label='Nro. de Aut. Fact./ DUI/Documento')
	tipo_d_documet = forms.CharField(max_length=100)
	nit_proveedor = forms.IntegerField()
	fecha_d_document_pago = forms.DateField(label='Fecha del documento de pago')
	razon_social_proveedor = forms.CharField(max_length=100)