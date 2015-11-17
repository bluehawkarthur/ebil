# from django.db import models
# from apps.proveedores.models import Proveedor

# class Item(models.Model):
# 	codigo_item = models.CharField(max_length=10)
# 	codigo_fabrica = models.CharField(max_length=10)
# 	almacen = models.IntegerField()
# 	grupo = models.CharField(max_length=50)
# 	subgrupo = models.CharField(max_length=50)
# 	descripcion = models.CharField(max_length=200)
# 	carac_especial_1 = models.CharField(max_length=50)
# 	carac_especial_2 = models.CharField(max_length=50)
# 	cantidad = models.IntegerField()
# 	saldo_min = models.IntegerField()
# 	proveedor = models.ForeignKey(Proveedor) #Relacion a la tabla de proveedores
# 	imagen = models.ImageField(upload_to='items')
# 	unidad_medida = models.CharField(max_length=20)
# 	costo_unitario = models.DecimalField(max_digits=5, decimal_places=3)

# 	def __unicode__(self):
# 		return self.codigo_item


