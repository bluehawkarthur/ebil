from django.db import models
import decimal
from apps.producto.models import Item
from apps.users.models import Personajuridica
from apps.config.models import Sucursal


# Create your models here.
class Venta(models.Model):
    # nro_factura = models.IntegerField()
    fecha = models.DateField()
    nit = models.BigIntegerField(null=True, blank=True)
    nro_factura = models.BigIntegerField(null=True, blank=True)
    razon_social = models.CharField(max_length=100)
    tipo_compra = models.CharField(max_length=100)
    cantidad_dias = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    recargo = models.DecimalField(max_digits=10, decimal_places=2)
    ice = models.DecimalField(max_digits=10, decimal_places=2)
    excentos = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
    numero_autorizacion = models.BigIntegerField(null=True, blank=True)
    llave_digital = models.CharField(max_length=200, null=True, blank=True)
    codigo_control = models.CharField(max_length=255, null=True, blank=True)
    fecha_limite = models.DateField(null=True, blank=True)
    tipo_movimiento = models.CharField(max_length=100, null=True, blank=True)
    nro_nota = models.BigIntegerField(null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, null=True, blank=True)
    actividad = models.CharField(max_length=200, null=True, blank=True)
    nro_baja = models.BigIntegerField(null=True, blank=True)
    # categoria = models.CharField(max_length=50)
    # movimiento = models.CharField(max_length=100)

    def __unicode__(self):
        return U" %s- %s" % (self.nit, self.razon_social)


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta)
    item = models.ForeignKey(Item, db_column='producto_id')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    recargo = models.DecimalField(max_digits=10, decimal_places=2)
    ice = models.DecimalField(max_digits=10, decimal_places=2)
    excentos = models.DecimalField(max_digits=10, decimal_places=2)
    scf = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.CharField(max_length=100)
    tipo_recargo = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.item


class Movimiento(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    detalle = models.CharField(max_length=100)
    fecha_transaccion = models.DateField()
    motivo_movimiento = models.CharField(max_length=100)
    item = models.ForeignKey(Item, db_column='producto_id')
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)


    def __unicode__(self):
        return self.motivo_movimiento


class Cobro(models.Model):
    venta = models.ForeignKey(Venta)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_transaccion = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Personajuridica, null=True, blank=True)
    nro = models.BigIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.venta.razon_social
