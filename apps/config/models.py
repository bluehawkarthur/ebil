from django.db import models
from apps.users.models import Personajuridica


class DatosDosificacion(models.Model):

	nro_conrelativo = models.BigIntegerField()
	fecha = models.DateField()
	nro_autorizacion = models.BigIntegerField()
	llave_digital = models.CharField(max_length=200)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
	contador = models.IntegerField()
