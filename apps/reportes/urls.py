from django.conf.urls import include, url
from .views import RepCompras, buscarProducto, RepVentas

urlpatterns = [
    url(r'^rep_compras/',  RepCompras.as_view(), name='rep_compras'),
    url(r'^rep_ventas/',  RepVentas.as_view(), name='rep_ventas'),
    url(r'^buscar_item/$', 'apps.reportes.views.buscarProducto'),

]
