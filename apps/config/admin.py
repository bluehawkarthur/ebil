from django.contrib import admin
from .models import DatosDosificacion, Formatofactura, ClienteCampos, AlmacenesCampos, ProveedoresCampos, FacturaCampos, Sucursal, Actividad

admin.site.register(DatosDosificacion)
admin.site.register(Formatofactura)
admin.site.register(ClienteCampos)
admin.site.register(AlmacenesCampos)
admin.site.register(ProveedoresCampos)
admin.site.register(FacturaCampos)
admin.site.register(Sucursal)
admin.site.register(Actividad)
