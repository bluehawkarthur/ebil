from django.db import models
from apps.config.models import Personajuridica
# Create your models here.


class BancarizacionCompras(models.Model):
	compra_fecha = models.DateField()
	modalidad_d_la_transaccion = models.CharField(max_length=100)
	nro_de_cta_doc_de_pago = models.IntegerField()  
	fecha_fact_dui_fecha_doc = models.DateField()
	monto_pagado_en_doc_d_pago = models.IntegerField()
	tipo_transaccion = models.CharField(max_length=100)
	monto_acumulado = models.IntegerField()
	nit_proveedor = models.IntegerField()
	nit_entidad_inanciera = models.IntegerField()
	razon_social_proveedor = models.CharField(max_length=100)
	nro_d_documento_de_pago = models.IntegerField()
	nro_d_fact_dui_nro_doc = models.IntegerField()
	tipo_de_doc_d_pago = models.CharField(max_length=100)
	tipo_de_documento = models.CharField(max_length=100)
	monto_fact_monto_dui_monto_doc = models.CharField(max_length=100)
	fecha_d_documento_d_pago = models.DateField()
	nro_de_aut_fact_dui_documento = models.IntegerField()
	empresa = models.ForeignKey(Personajuridica, null=True)


	def __unicode__(self):
		return self.razon_social_proveedor


class BancarizacionVentas(models.Model):
	venta_fecha = models.DateField()
	modalidad_d_la_transaccion = models.CharField(max_length=100)
	nro_de_cta_doc_de_pago = models.IntegerField()  
	fecha_fact_dui_fecha_doc = models.DateField()
	monto_pagado_en_doc_d_pago = models.IntegerField()
	tipo_transaccion = models.CharField(max_length=100)
	monto_acumulado = models.IntegerField()
	nro_d_fact_dui_nro_doc = models.IntegerField()
	nit_entidad_inanciera = models.IntegerField()
	monto_fact_monto_doc = models.CharField(max_length=100)
	nro_d_documento_de_pago = models.IntegerField()
	nro_de_auturizacion_d_fact = models.IntegerField()
	tipo_de_doc_d_pago = models.CharField(max_length=100)
	tipo_de_documento = models.CharField(max_length=100)
	nit_ci_d_cliente = models.IntegerField()
	fecha_d_documento_d_pago = models.DateField()
	razon_social_cliente = models.CharField(max_length=100)
	empresa = models.ForeignKey(Personajuridica, null=True)


	def __unicode__(self):
		return self.razon_social_cliente