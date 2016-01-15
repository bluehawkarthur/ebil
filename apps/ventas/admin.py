from django.contrib import admin
from .models import Venta, DetalleVenta, Movimiento, Cobro

# Register your models here.
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Movimiento)
admin.site.register(Cobro)
