from django.db import models
from apps.users.models import Personajuridica

# Create your models here.
class Cliente(models.Model):
	codigo = models.CharField(max_length=50, null=True, blank=True)
	razonsocial = models.CharField(max_length=50)
	nit = models.BigIntegerField()
	direccion = models.CharField(max_length=50, null=True, blank=True)
	telefonos1 = models.CharField(max_length=8, null=True, blank=True)
	telefonos2 = models.CharField(max_length=8, null=True, blank=True)
	telefonos3 = models.CharField(max_length=8, null=True, blank=True)
	contacto = models.CharField(max_length=50, null=True, blank=True)
	rubro = models.CharField(max_length=50, null=True, blank=True)
	categoria = models.CharField(max_length=50, null=True, blank=True)
	ubucaciongeo = models.CharField(max_length=50, null=True, blank=True)
	fecha = models.DateField(null=True, blank=True)
	fecha2 = models.DateField(null=True, blank=True)
	textos = models.CharField(max_length=50, null=True, blank=True)
	textos2 = models.CharField(max_length=50, null=True, blank=True)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)

	class Meta:
		unique_together = ('codigo', 'nit',)

	def __unicode__(self):
		return self.contacto

