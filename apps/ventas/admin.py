from django.contrib import admin
from .models import Venta, DetalleVenta, Movimiento, Cobro

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 2


class FacturaAdmin(admin.ModelAdmin):
    
    inlines = [DetalleFacturaInline]

# Register your models here.
admin.site.register(Venta, FacturaAdmin)
admin.site.register(DetalleVenta)
admin.site.register(Movimiento)
admin.site.register(Cobro)
