from django.db import models
from apps.users.models import Personajuridica


class Sucursal(models.Model):
	nombre_sucursal = models.CharField(max_length=100)
	nro_sucursal = models.BigIntegerField()
	direccion = models.CharField(max_length=100)
	telefono1 = models.IntegerField()
	telefono2 = models.IntegerField(null=True)
	telefono3 = models.IntegerField(null=True)
	departamento = models.CharField(max_length=100)
	municipios = models.CharField(max_length=100)
	empresa = models.ForeignKey(Personajuridica, null=True)

	def __unicode__(self):
		return self.nombre_sucursal


class Actividad(models.Model):
	actividad = models.CharField(max_length=100)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)

	def __unicode__(self):
		return self.actividad


class DatosDosificacion(models.Model):

	nro_conrelativo = models.BigIntegerField()
	fecha = models.DateField()
	nro_autorizacion = models.BigIntegerField()
	llave_digital = models.CharField(max_length=200)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
	contador = models.IntegerField()
	sucursal = models.ForeignKey(Sucursal, null=True, blank=True)
	actividad = models.ForeignKey(Actividad, null=True, blank=True)


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


class Formatodetalle(models.Model):
	impresion = models.CharField(max_length=100)
	facturacion = models.CharField(max_length=100)
	tamanio = models.CharField(max_length=100)
	frases_titulo = models.CharField(max_length=100)
	frases_subtitulo = models.CharField(max_length=100)
	frases_pie = models.CharField(max_length=200)
	formatofact = models.ForeignKey(Formatofactura, null=True, blank=True)
	sucursal = models.ForeignKey(Sucursal, null=True, blank=True)

	def __unicode__(self):
		return self.formatofact.formato


class ClienteCampos(models.Model):
	direccion_usar = models.BooleanField()
	direccion_requerido = models.BooleanField()
	direccion_tipo = models.CharField(max_length=100)
	direccion_caractr = models.IntegerField()
	telefono1_usar = models.BooleanField()
	telefono1_requerido = models.BooleanField()
	telefono1_tipo = models.CharField(max_length=100)
	telefono1_caractr = models.IntegerField()
	telefono2_usar = models.BooleanField()
	telefono2_requerido = models.BooleanField()
	telefono2_tipo = models.CharField(max_length=100)
	telefono2_caractr = models.IntegerField()
	telefono3_usar = models.BooleanField()
	telefono3_requerido = models.BooleanField()
	telefono3_tipo = models.CharField(max_length=100)
	telefono3_caractr = models.IntegerField()
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
	fecha_usar = models.BooleanField()
	fecha_requerido = models.BooleanField()
	fecha2_usar = models.BooleanField()
	fecha2_requerido = models.BooleanField()
	texto_usar = models.BooleanField()
	texto_requerido = models.BooleanField()
	texto_tipo = models.CharField(max_length=100)
	texto_caractr = models.IntegerField()
	texto2_usar = models.BooleanField()
	texto2_requerido = models.BooleanField()
	texto2_tipo = models.CharField(max_length=100)
	texto2_caractr = models.IntegerField()
	empresa = models.ForeignKey(Personajuridica, null=True)


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


class ProveedoresCampos(models.Model):
	direccion_usar = models.BooleanField()
	direccion_requerido = models.BooleanField()
	direccion_tipo = models.CharField(max_length=100)
	direccion_caractr = models.IntegerField()
	telefonos1_usar = models.BooleanField()
	telefonos1_requerido = models.BooleanField()
	telefonos1_tipo = models.CharField(max_length=100)
	telefonos1_caractr = models.IntegerField()
	telefonos2_usar = models.BooleanField()
	telefonos2_requerido = models.BooleanField()
	telefonos2_tipo = models.CharField(max_length=100)
	telefonos2_caractr = models.IntegerField()
	telefonos3_usar = models.BooleanField()
	telefonos3_requerido = models.BooleanField()
	telefonos3_tipo = models.CharField(max_length=100)
	telefonos3_caractr = models.IntegerField()
	contacto_usar = models.BooleanField()
	contacto_requerido = models.BooleanField()
	contacto_tipo = models.CharField(max_length=100)
	contacto_caractr = models.IntegerField()
	rubro_usar = models.BooleanField()
	rubro_requerido = models.BooleanField()
	rubro_tipo = models.CharField(max_length=100)
	rubro_caractr = models.IntegerField()
	ubicacion_geo_usar = models.BooleanField()
	ubicacion_geo_requerido = models.BooleanField()
	ubicacion_geo_tipo = models.CharField(max_length=100)
	ubicacion_geo_caractr = models.IntegerField()
	fechas_usar = models.BooleanField()
	fechas_requerido = models.BooleanField()
	fechas2_usar = models.BooleanField()
	fechas2_requerido = models.BooleanField()
	textos_usar = models.BooleanField()
	textos_requerido = models.BooleanField()
	textos_tipo = models.CharField(max_length=100)
	textos_caractr = models.IntegerField()
	textos2_usar = models.BooleanField()
	textos2_requerido = models.BooleanField()
	textos2_tipo = models.CharField(max_length=100)
	textos2_caractr = models.IntegerField()
	empresa = models.ForeignKey(Personajuridica, null=True)


class FacturaCampos(models.Model):
	descuento_usar = models.BooleanField()
	descuento_requerido = models.BooleanField()
	recargo_usar = models.BooleanField()
	recargo_requerido = models.BooleanField()
	ice_usar = models.BooleanField()
	ice_requerido = models.BooleanField()
	exentos_usar = models.BooleanField()
	exentos_requerido = models.BooleanField()
	tipos_venta_usar = models.BooleanField()
	tipos_venta_requerido = models.BooleanField()
	empresa = models.ForeignKey(Personajuridica, null=True)
