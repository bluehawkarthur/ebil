from django.conf.urls import include, url
from .views import RepCompras, buscarProducto, RepVentas, Reporteventa

urlpatterns = [
    url(r'^rep_compras/',  RepCompras.as_view(), name='rep_compras'),
    url(r'^rep_ventas/',  RepVentas.as_view(), name='rep_ventas'),
    url(r'^buscar_item/$', 'apps.reportes.views.buscarProducto'),
    url(r'^reporte_venta/',  Reporteventa.as_view(), name='reporteventa'),

]
