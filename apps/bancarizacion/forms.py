# -*- coding: utf-8 -*-
from django import forms, http
from .models import BancarizacionCompras, BancarizacionVentas
from django.forms import ModelForm
from .models import BancarizacionCompras, BancarizacionVentas
# Create your models here.

class BancarizacionComprasForm(forms.ModelForm):
	compra_fecha = forms.DateField()
	modalidad_d_la_transaccion = forms.CharField(max_length=100, label='Modalidad de  la transacción')
	nro_de_cta_doc_de_pago = forms.IntegerField(label='Nro. De Cta. Doc. de pago')  
	fecha_fact_dui_fecha_doc = forms.DateField(label='Fecha fact. DUI/Fecha Doc.')
	monto_pagado_en_doc_d_pago = forms.IntegerField(label='Monto pagado en Doc. De pago')
	tipo_transaccion = forms.CharField(max_length=100, label='Tipo Transacción')
	monto_acumulado = forms.IntegerField(label='Monto acumulado')
	nit_proveedor = forms.IntegerField(label='NIT Proveedor')
	nit_entidad_inanciera = forms.IntegerField(label='NIT Entidad Financiera')
	razon_social_proveedor = forms.CharField(max_length=100, label='Razón Social Proveedor')
	nro_d_documento_de_pago = forms.IntegerField(label='Nro. de Documento de pago')
	nro_d_fact_dui_nro_doc = forms.IntegerField(label='Nro. De fact. DUI/Nro. Doc.')
	1
	tipo_de_doc_d_pago= forms.CharField(max_length=100)
	tipo_de_documento = forms.CharField(max_length=100, label='Tipo de documento')
	monto_fact_monto_dui_monto_doc = forms.CharField(max_length=100, label='Monto fact./Monto DUI/Monto Doc.')
	fecha_d_documento_d_pago = forms.DateField(label='Fecha del documento de pago')
	nro_de_aut_fact_dui_documento = forms.IntegerField(label='Nro. de Aut. Fact./ DUI/Documento')

	class Meta:
		model = BancarizacionCompras
		fields = [
'compra_fecha', 'modalidad_d_la_transaccion', 'nro_de_cta_doc_de_pago', 'fecha_fact_dui_fecha_doc', 'monto_pagado_en_doc_d_pago',
'tipo_transaccion', 'monto_acumulado', 'nit_proveedor',
'nit_entidad_inanciera', 'razon_social_proveedor', 'nro_d_documento_de_pago', 'nro_d_fact_dui_nro_doc', 'tipo_de_doc_d_pago', 'tipo_de_documento',
'monto_fact_monto_dui_monto_doc', 'fecha_d_documento_d_pago', 'nro_de_aut_fact_dui_documento']
			


class BancarizacionVentasForm(forms.Form):
	venta_fecha = forms.DateField()
	modalidad_d_la_transaccion = forms.CharField(max_length=100, label='Modalidad de  la transacción')
	nro_de_cta_doc_de_pago = forms.IntegerField(label='Nro. De Cta. Doc. de pago')  
	fecha_fact_dui_fecha_doc = forms.DateField(label='Fecha fact. DUE/Fecha Doc.')
	monto_pagado_en_doc_d_pago = forms.IntegerField(label='Monto pagado en Doc. De pago')
	tipo_transaccion = forms.CharField(max_length=100, label='Tipo Transacción')
	monto_acumulado = forms.IntegerField(label='Monto acumulado')
	nro_d_fact_dui_nro_doc = forms.IntegerField(label='Nro. De fact. DUE/Nro. Doc.')
	nit_entidad_inanciera = forms.IntegerField(label='NIT Entidad Financiera')
	monto_fact_monto_doc = forms.IntegerField(label='Monto fact./Monto Doc.')
	nro_d_documento_de_pago = forms.IntegerField(label='Nro. de Documento de pago')
	nro_de_auturizacion_d_fact = forms.IntegerField(label='Nro. de Autorización de la Fact.')
	tipo_de_doc_d_pago = forms.CharField(max_length=100)
	tipo_de_documento = forms.CharField(max_length=100, label='Tipo de documento')
	nit_ci_d_cliente = forms.IntegerField(label='NIT/CI del cliente')
	fecha_d_documento_d_pago = forms.DateField(label='Fecha del documento de pago')
	razon_social_cliente = forms.CharField(max_length=100, label='Razón Social Cliente')