from django.db import models
from apps.config.models import Personajuridica
# Create your models here.

class Bancarizacion(models.Model):
	compra_fecha = models.DateField()
	venta_fecha = models.DateField()
	modal_transacc = models.CharField(max_length=100)
	nro_d_cta_doc_de_pago = models.IntegerField()
	fecha_fact_due_fec_doc = models.DateField()
	monto_pagado_en_doc_d_pago = models.IntegerField()
	tipo_transaccion = models.CharField(max_length=100)
	monto_acumulado = models.IntegerField()
	nro_d_fact_due_nro_doc = models.CharField(max_length=100)
	nit_entidad_financiera = models.IntegerField()
	monto_fact_monto_doc = models.IntegerField()
	nro_d_docment_pago = models.IntegerField()
	nro_d_autoriza_de_fect = models.IntegerField()
	tipo_d_documet = models.CharField(max_length=100)
	nit_proveedor = models.IntegerField()
	fecha_d_document_pago = models.DateField()
	razon_social_proveedor = models.CharField(max_length=100)
	empresa = models.ForeignKey(Personajuridica, null=True)

	
	def __unicode__(self):
		return self.razon_social_cliente