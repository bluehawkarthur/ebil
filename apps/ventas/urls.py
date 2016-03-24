from django.conf.urls import url

urlpatterns = [
    url(r'^ventas/$', 'apps.ventas.views.ventaCrear', name='registrarventas'),
    url(r'^buscar_item2/$', 'apps.ventas.views.buscarProducto'),
    url(r'^buscar_cliente/$', 'apps.ventas.views.buscarCliente'),
    url(r'^detalle_venta/(?P<pk>\d+)$', 'apps.ventas.views.detalleVenta', name='detalleventa'),
    url(r'^detalle_ventanota/(?P<pk>\d+)$', 'apps.ventas.views.detalleVentaNota', name='detalleventanota'),
    # url(r'^detalle_ventarollo/(?P<pk>\d+)$', 'apps.ventas.views.detalleVentarollo', name='detalleventarollo'),
    url(r'^migrate/$', 'apps.ventas.views.migrate'),
]
