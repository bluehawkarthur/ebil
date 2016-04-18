from django.db import models
from apps.proveedores.models import Proveedor
from django.conf import settings

from apps.users.models import Personajuridica


class ItemManager(models.Manager):
    def get_by_natural_key(self, descripcion, precio_unitario):
        return self.get(codigo_item=codigo_item, descripcion=descripcion, precio_unitario=precio_unitario, unidad_medida=unidad_medida)


class Item(models.Model):
	objects = ItemManager()

	codigo_item = models.CharField(max_length=100, unique=True)
	codigo_fabrica = models.CharField(max_length=100, blank=True, null=True)
	almacen = models.IntegerField()
	grupo = models.CharField(max_length=100, blank=True, null=True)
	subgrupo = models.CharField(max_length=100, blank=True, null=True)
	descripcion = models.CharField(max_length=200)
	carac_especial_1 = models.CharField(max_length=100, blank=True, null=True)
	carac_especial_2 = models.CharField(max_length=100, blank=True, null=True)
	cantidad = models.IntegerField()
	saldo_min = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor, related_name='proveedor', blank=True, null=True) #Relacion a la tabla de proveedores
	imagen = models.ImageField(upload_to='items', null=True, blank=True)
	unidad_medida = models.CharField(max_length=100)
	costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
	precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
	empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
	fecha_transaccion = models.DateField(null=True, blank=True)

	# class Meta:
	# 	unique_together = ('codigo_item', 'carac_especial_1', 'carac_especial_2', 'cantidad',)
	
	def natural_key(self):
		return (self.codigo_item, self.descripcion, self.precio_unitario, self.unidad_medida)

	def __unicode__(self):
		return "%s-%s" % (self.codigo_item, self.descripcion)



