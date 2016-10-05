from django.db import models
from apps.users.models import Personajuridica
# Create your models here.


class Proveedor(models.Model):
    codigo = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=150)
    nit = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono1 = models.IntegerField(null=True)
    telefono2 = models.IntegerField(null=True)
    telefono3 = models.IntegerField(null=True)
    contactos = models.CharField(max_length=150)
    rubro = models.CharField(max_length=50)
    ubicacion_geo = models.CharField(max_length=50)
    fecha1 = models.DateField(null=True)
    fecha2 = models.DateField(null=True)
    texto1 = models.CharField(max_length=50, null=True)
    texto2 = models.CharField(max_length=50, null=True)
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)

    class Meta:
    	unique_together = ('codigo', 'empresa',)

    def __unicode__(self):
        return self.razon_social

