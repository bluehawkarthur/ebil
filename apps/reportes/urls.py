from django.conf.urls import include, url
from .views import RepCompras, buscarProducto, RepVentas, Reporteventa, ReportVendetalle

urlpatterns = [
    url(r'^rep_compras/',  RepCompras.as_view(), name='rep_compras'),
    url(r'^rep_ventas/',  RepVentas.as_view(), name='rep_ventas'),
    url(r'^buscar_item/$', 'apps.reportes.views.buscarProducto'),
    url(r'^reporte_venta/',  Reporteventa.as_view(), name='reporteventa'),
    url(r'^rep_ventadet/$',  'apps.reportes.views.ReportVendetalle', name='reporteventadet'),
    url(r'^rep_detalle_venta/(?P<pk>\d+)$', 'apps.reportes.views.detalleVenta', name='repdetalleventa'),
    url(r'^excel/$',  'apps.reportes.views.excel', name='excel'),
    url(r'^buscar_empresa/$', 'apps.reportes.views.buscarEmpresa'),

    # url(r'^pdf/$', 'apps.reportes.views.pdf'),
    # url(r'^pdf2/$', 'apps.reportes.views.generar_pdf'),

]
