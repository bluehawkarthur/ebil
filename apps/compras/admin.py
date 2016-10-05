from django.contrib import admin
from .models import Compra, DetalleCompra, CentroCostos
# Register your models here.

admin.site.register(Compra)
admin.site.register(DetalleCompra)
admin.site.register(CentroCostos)
