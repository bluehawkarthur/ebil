from django.conf.urls import url

urlpatterns = [
    url(r'^ventas/$', 'apps.ventas.views.ventaCrear', name='registrarventas'),
    url(r'^buscar_item2/$', 'apps.ventas.views.buscarProducto'),
    url(r'^detalle_venta/(?P<pk>\d+)$', 'apps.ventas.views.detalleVenta', name='detalleventa'),
]
