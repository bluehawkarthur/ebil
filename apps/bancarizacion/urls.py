from django.conf.urls import include, url
from .views import ListarBancarizacionCompras, DetalleBancarizacionCompras, EditBancarizacionCompras, DeleteBancarizacionCompras
from .views import ListarBancarizacionVentas, DetalleBancarizacionVentas, EditBancarizacionVentas, DeleteBancarizacionVentas

# import debug_toolbar
urlpatterns = [
    url(r'^crear_bancar/$', 'apps.bancarizacion.views.CrearBancarizacionCompras', name='crear_bancar'),
    url(r'^listar_Bancarizacion/', ListarBancarizacionCompras.as_view(), name='listar_Bancarizacion'),
    url(r'^detalle_bancarizacion/(?P<pk>\d+)$', DetalleBancarizacionCompras.as_view(), name='detalle_bancarizacion'),
    url(r'^edit_bancarizacion/(?P<pk>\d+)$', EditBancarizacionCompras.as_view(), name='edit_bancarizacion'),
    url(r'^delete_bancarizacion/(?P<bancarizacion>\d+)$', 'apps.bancarizacion.views.DeleteBancarizacionCompras', name='bancarizacion_delete'),
    url(r'^libro_bancar/', 'apps.bancarizacion.views.Libro_BancarizacionCompras', name='libro_bancar'),
    # bacari ventas
    url(r'^crear_bancar_ventas/$', 'apps.bancarizacion.views.CrearBancarizacionVentas', name='crear_bancar_ventas'),
    url(r'^listar_Bancar_ventas/', ListarBancarizacionVentas.as_view(), name='listar_Bancar_ventas'),
    url(r'^detalle_Bancar_ventas/(?P<pk>\d+)$', DetalleBancarizacionVentas.as_view(), name='detalle_Bancar_ventas'),
    url(r'^edit_Bancar_ventas/(?P<pk>\d+)$', EditBancarizacionVentas.as_view(), name='edit_Bancar_ventas'),
    url(r'^delete_bancar_venta/(?P<bancarizacion>\d+)$', 'apps.bancarizacion.views.DeleteBancarizacionVentas', name='bancarizacion_delete'),
    url(r'^libro_bancar_venta/', 'apps.bancarizacion.views.Libro_BancarizacionVentas', name='libro_bancar_venta'),
]