from django.conf.urls import patterns, include, url
from .views import CrearCliente, ListarCliente, DetalleCliente, EditCliente

urlpatterns = patterns('',
	url(r'^CrearCliente/', CrearCliente.as_view(), name='CrearCliente'),
	url(r'^listar_cliente/', ListarCliente.as_view(), name='listar_cliente'),
	url(r'^detalle_cliente/(?P<pk>\d+)$', DetalleCliente.as_view(), name='detalle_cliente'),
	url(r'^editar_cliente/(?P<pk>\d+)$', EditCliente.as_view(), name='editar_cliente'),
    url(r'^delete_cliente/(?P<id>\d+)$', 'apps.cliente.views.eliminar', name='delete'),
)