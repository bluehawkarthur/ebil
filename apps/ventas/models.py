from django.db import models
import decimal
from apps.producto.models import Item

# Create your models here.
class Venta(models.Model):
    # nro_factura = models.IntegerField()
    fecha = models.DateField()
    nit = models.IntegerField()
    razon_social = models.CharField(max_length=100)
    tipo_compra = models.CharField(max_length=100)
    cantidad_dias = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    # categoria = models.CharField(max_length=50)
    # movimiento = models.CharField(max_length=100)

    def __unicode__(self):
        return U" %s- %s" % (self.nit, self.razon_social)


class DetalleVenta(models.Model):
	venta = models.ForeignKey(Venta)
	item = models.ForeignKey(Item, db_column='producto_id')
	cantidad = models.IntegerField()
	subtotal = models.DecimalField(max_digits=6, decimal_places=2)
	descuento = models.DecimalField(max_digits=6, decimal_places=2)
	recargo = models.DecimalField(max_digits=6, decimal_places=2)
	ice = models.DecimalField(max_digits=6, decimal_places=2)
	excentos = models.DecimalField(max_digits=6, decimal_places=2)
	scf = models.DecimalField(max_digits=6, decimal_places=2) #sub total
	tipo_descuento = models.CharField(max_length=100)
	tipo_recargo = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % self.item