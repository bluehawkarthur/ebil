from django.db import models
from django.conf import settings

# Create your models here.
class Cliente(models.Model):
	codigo = models.IntegerField()
	razonSocial = models.CharField(max_length=50)
	nit = models.IntegerField()
	Direccion = models.CharField(max_length=50)
	telefonos1 = models.IntegerField()
	telefonos2 = models.IntegerField()
	telefonos3 = models.IntegerField()
	contacto = models.CharField(max_length=50)
	rubro = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	UbucacionGeo = models.CharField(max_length=50) 
	fecha = models.DateField()
	fecha2 = models.DateField()
	textos = models.CharField(max_length=50)
	textos2 = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.contacto