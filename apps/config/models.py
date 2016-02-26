from django.db import models
from apps.users.models import Personajuridica


class DatosDosificacion(models.Model):

	nro_conrelativo = models.BigIntegerField()
	fecha = models.DateField()
	nro_autorizacion = models.BigIntegerField()
	llave_digital = models.CharField(max_length=200)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
	contador = models.IntegerField()


class Formatofactura(models.Model):
	formato = models.CharField(max_length=100)
	impresion = models.CharField(max_length=100)
	facturacion = models.CharField(max_length=100)
	tamanio = models.CharField(max_length=100)
	frases_titulo = models.CharField(max_length=100)
	frases_subtitulo = models.CharField(max_length=100)
	frases_pie = models.CharField(max_length=200)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)

	def __unicode__(self):
		return self.empresa.razon_social
