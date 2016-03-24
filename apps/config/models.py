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


class ClienteCampos(models.Model):
	codigo_usar = models.BooleanField()
	codigo_requerido = models.BooleanField()
	codigo_tipo = models.CharField(max_length=100)
	codigo_caractr = models.IntegerField()
	razonsocal_usar = models.BooleanField()
	razonsocal_requerido = models.BooleanField()
	razonsocal_tipo = models.CharField(max_length=100)
	razonsocal_caractr = models.IntegerField()
	nit_usar = models.BooleanField()
	nit_requerido = models.BooleanField()
	nit_tipo = models.CharField(max_length=100)
	nit_caractr = models.IntegerField()
	direccion_usar = models.BooleanField()
	direccion_requerido = models.BooleanField()
	direccion_tipo = models.CharField(max_length=100)
	direccion_caractr = models.IntegerField()
	telefonos_usar = models.BooleanField()
	telefonos_requerido = models.BooleanField()
	telefonos_tipo = models.CharField(max_length=100)
	telefonos_caractr = models.IntegerField()
	contacto_usar = models.BooleanField()
	contacto_requerido = models.BooleanField()
	contacto_tipo = models.CharField(max_length=100)
	contacto_caractr = models.IntegerField()
	rubro_usar = models.BooleanField()
	rubro_requerido = models.BooleanField()
	rubro_tipo = models.CharField(max_length=100)
	rubro_caractr = models.IntegerField()
	categoria_usar = models.BooleanField()
	categoria_requerido = models.BooleanField()
	categoria_tipo = models.CharField(max_length=100)
	categoria_caractr = models.IntegerField()
	ubicaciongeo_usar = models.BooleanField()
	ubicaciongeo_requerido = models.BooleanField()
	ubicaciongeo_tipo = models.CharField(max_length=100)
	ubicaciongeo_caractr = models.IntegerField()
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)


class AlmacenesCampos(models.Model):
	codigo_fabr_usar = models.BooleanField()
	codigo_fabr_reque = models.BooleanField()
	codigo_fabricatipo = models.CharField(max_length=100)
	codigo_fabricacaractr = models.IntegerField()
	caract_espec_usar = models.BooleanField()
	caract_espec_requerid = models.BooleanField()
	caract_espectipo = models.CharField(max_length=100)
	caract_especaractr = models.IntegerField()
	unidad_medid_usar = models.BooleanField()
	unidad_medid_requerido = models.BooleanField()
	unidad_medidatipo = models.CharField(max_length=100)
	unidad_medidacaractr = models.IntegerField()
	imagen_usar = models.BooleanField()
	imagen_requer = models.BooleanField()
	grupo_usar = models.BooleanField()
	grupo_requerido = models.BooleanField()
	grupo_tipo = models.CharField(max_length=100)
	grupo_caractr = models.IntegerField()
	subgrupo_usar = models.BooleanField()
	subgrupo_requerido = models.BooleanField()
	subgrupo_tipo = models.CharField(max_length=100)
	subgrupo_caractr = models.IntegerField()
	carac_especial_2_usar = models.BooleanField()
	carac_especial_2_requerido = models.BooleanField()
	carac_especial_2_tipo = models.CharField(max_length=100)
	carac_especial_2_caractr = models.IntegerField()
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)


