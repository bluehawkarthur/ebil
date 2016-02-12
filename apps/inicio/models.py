from django.db import models
from django.conf import settings


class Rol(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	modelos = models.CharField(max_length=100)
	operar = models.BooleanField()
	crear = models.BooleanField()
	editar = models.BooleanField()
	eliminar = models.BooleanField()

	def __unicode__(self):
		return self.modelos
