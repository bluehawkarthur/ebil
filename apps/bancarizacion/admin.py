from django.contrib import admin
from .models import BancarizacionCompras, BancarizacionVentas
# Register your models here.
admin.site.register(BancarizacionCompras)
admin.site.register(BancarizacionVentas)