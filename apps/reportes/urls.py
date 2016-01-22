from django.conf.urls import include, url
from .views import RepCompras, buscarProducto, RepVentas, Reporteventa, ReportVendetalle, ReporteCaja

urlpatterns = [
    url(r'^rep_compras/', RepCompras.as_view(), name='rep_compras'),
    url(r'^rep_ventas/', RepVentas.as_view(), name='rep_ventas'),
    url(r'^buscar_item/$', 'apps.reportes.views.buscarProducto'),
    url(r'^reporte_venta/', 'apps.reportes.views.Reporteventa', name='reporteventa'),
    url(r'^rep_ventadet/$', 'apps.reportes.views.ReportVendetalle', name='reporteventadet'),
    url(r'^rep_detalle_venta/(?P<pk>\d+)$', 'apps.reportes.views.detalleVenta', name='repdetalleventa'),
    # url(r'^excel/$',  'apps.reportes.views.excel', name='excel'),
    url(r'^buscar_empresa/$', 'apps.reportes.views.buscarEmpresa'),
    url(r'^rep_ventaMes/', 'apps.reportes.views.report_mesVenta', name='rep_ventaMes'),
    url(r'^rep_almacenes/', 'apps.reportes.views.report_almacenes', name='rep_almacenes'),
    url(r'^libro_compras/', 'apps.reportes.views.libro_compras', name='libro_compras'),
    url(r'^libro_ventas/', 'apps.reportes.views.libro_ventas', name='libro_ventas'),
    url(r'^reporte_almacen/', 'apps.reportes.views.ReportAlmacen', name='reporte_almacen'),
    url(r'^kardex_almacen/(?P<pk>\d+)/(?P<date1>[\w-]+)/(?P<anio>[\w-]+)/$', 'apps.reportes.views.promedios', name='kardex_almacen'),
    url(r'^create_pago/', 'apps.reportes.views.Createpago', name='create_pago'),
    # url(r'^pdf/$', 'apps.reportes.views.pdf'),
    # url(r'^pdf2/$', 'apps.reportes.views.generar_pdf'),
    url(r'^caja/$', ReporteCaja.as_view(), name='rep_caja'),

]
