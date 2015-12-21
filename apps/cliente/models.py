from django.db import models
from django.conf import settings

from django.core.validators import RegexValidator

# Create your models here.
class Cliente(models.Model):
	codigo = models.CharField(max_length=50)
	razonsocial = models.CharField(max_length=50)
	nit = models.BigIntegerField()
	direccion = models.CharField(max_length=50)
	telefonos1 = models.CharField(max_length=8)
	telefonos2 = models.CharField(max_length=8)
	telefonos3 = models.CharField(max_length=8)
	contacto = models.CharField(max_length=50)
	rubro = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	ubucaciongeo = models.CharField(max_length=50) 
	fecha = models.DateField()
	fecha2 = models.DateField()
	textos = models.CharField(max_length=50)
	textos2 = models.CharField(max_length=50)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.contacto

