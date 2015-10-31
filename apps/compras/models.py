from django.db import models
import decimal
from apps.producto.models import Item

# Create your models here.


class Compra(models.Model):
    nit = models.IntegerField()
    razon_social = models.CharField(max_length=6)
    nro_factura = models.IntegerField()
    nro_autorizacion = models.IntegerField()
    fecha = models.DateTimeField()
    monto = models.IntegerField()
    descuento = models.IntegerField()
    recargo = models.IntegerField()
    ice = models.IntegerField()
    excentos = models.IntegerField()
    cod_control = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    class Meta:

        # no duplicate serie y numero juntos
        unique_together = (('nit', 'nro_factura'),)

    def __unicode__(self):
        return U" %s- %s" % (self.nit, self.nro_factura)


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, db_column='compra_id')
    producto = models.ForeignKey(Item, db_column='producto_id')
    codigo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=10)
    detalle = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    descuento = models.IntegerField()
    recargo = models.IntegerField()
    ice = models.IntegerField()
    excentos = models.IntegerField()
    cf = models.IntegerField()
    centro_costos = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.detalle