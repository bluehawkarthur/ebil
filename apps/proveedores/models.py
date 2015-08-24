from django.db import models

# Create your models here.
class Proveedor(models.Model):
	codigo = models.CharField(max_length=20)
	razon_social = models.CharField(max_length=150)
	nit = models.CharField(max_length=20)
	direccion = models.CharField(max_length=50)
	telefono1 = models.IntegerField()
	telefono2 = models.IntegerField()
	telefono3 = models.IntegerField()
	contactos = models.CharField(max_length=150)
	rubro = models.CharField(max_length=50)
	ubicacion_geo = models.CharField(max_length=50)
	fecha1 = models.DateField()
	fecha2 = models.DateField()
	texto1 = models.CharField(max_length=50)
	texto2 = models.CharField(max_length=50)

	def __unicode__(self):
		return self.razon_social

