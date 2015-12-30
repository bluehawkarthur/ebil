from django.db import models
import decimal
from apps.producto.models import Item

# Create your models here.


class Compra(models.Model):
    nit = models.BigIntegerField()
    razon_social = models.CharField(max_length=100)
    nro_factura = models.IntegerField()
    nro_autorizacion = models.CharField(max_length=20)
    fecha = models.DateField()
    cod_control = models.CharField(max_length=100)
    tipo_compra = models.CharField(max_length=100)
    cantidad_dias = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    recargo = models.DecimalField(max_digits=6, decimal_places=2)
    ice = models.DecimalField(max_digits=6, decimal_places=2)
    excentos = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)

    def __unicode__(self):
        return U" %s- %s" % (self.nit, self.nro_factura)


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, db_column='compra_id')
    producto = models.ForeignKey(Item, db_column='producto_id', null=True, blank=True)
    codigo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=10)
    detalle = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    recargo = models.DecimalField(max_digits=6, decimal_places=2)
    ice = models.DecimalField(max_digits=6, decimal_places=2)
    excentos = models.DecimalField(max_digits=6, decimal_places=2)
    scf = models.DecimalField(max_digits=6, decimal_places=2)
    centro_costos = models.CharField(max_length=100)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.detalle