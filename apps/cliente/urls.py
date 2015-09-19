from django.conf.urls import patterns, include, url
from .views import CrearCliente, ListarCliente, DetalleCliente, EditCliente, DeleteCliente

urlpatterns = patterns('',
	url(r'^CrearCliente/', CrearCliente.as_view(), name='CrearCliente'),
	url(r'^listar_cliente/', ListarCliente.as_view(), name='listar_cliente'),
	url(r'^detalle_Cliente/(?P<pk>\d+)$', DetalleCliente.as_view(), name='detalle_Cliente'),
	url(r'^editar_Cliente/(?P<pk>\d+)$', EditCliente.as_view(), name='editar_Cliente'),
	url(r'^delete_Cliente/(?P<pk>\d+)$', DeleteCliente.as_view(), name='delete_Cliente'),
)