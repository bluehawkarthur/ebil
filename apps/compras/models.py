from django.db import models
import decimal
from apps.producto.models import Item
from apps.users.models import Personajuridica
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
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    recargo = models.DecimalField(max_digits=10, decimal_places=2)
    ice = models.DecimalField(max_digits=10, decimal_places=2)
    excentos = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
    monto_pago = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    nro_nota = models.BigIntegerField(null=True, blank=True)

    def __unicode__(self):
        return U" %s- %s" % (self.nit, self.nro_factura)


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, db_column='compra_id')
    producto = models.ForeignKey(Item, db_column='producto_id', null=True, blank=True)
    codigo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=10)
    detalle = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    recargo = models.DecimalField(max_digits=10, decimal_places=2)
    ice = models.DecimalField(max_digits=10, decimal_places=2)
    excentos = models.DecimalField(max_digits=10, decimal_places=2)
    scf = models.DecimalField(max_digits=10, decimal_places=2)
    centro_costos = models.CharField(max_length=100)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.detalle


class CentroCostos(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    cod = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.descripcion

class CobroCompra(models.Model):
    compra = models.ForeignKey(Compra)
    monto_pago = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fecha_transaccion = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.compra.razon_social
