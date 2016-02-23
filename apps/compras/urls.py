from django.conf.urls import url
from .views import Success

urlpatterns = [
    url(r'^compras/$', 'apps.compras.views.compraCrear', name='registrar'),
    url(r'^success/$', Success.as_view(), name='success'),
    url(r'^buscar_item/$', 'apps.compras.views.buscarProducto'),
    url(r'^buscar_proveedor/$', 'apps.compras.views.buscarProveedor'),
    url(r'^detalle_compra/(?P<pk>\d+)$', 'apps.compras.views.detalleCompra', name='detallecompra'),
]
