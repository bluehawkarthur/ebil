from django.contrib import admin
from .models import DatosDosificacion, Formatofactura, ClienteCampos, AlmacenesCampos, ProveedoresCampos, FacturaCampos

admin.site.register(DatosDosificacion)
admin.site.register(Formatofactura)
admin.site.register(ClienteCampos)
admin.site.register(AlmacenesCampos)
admin.site.register(ProveedoresCampos)
admin.site.register(FacturaCampos)
