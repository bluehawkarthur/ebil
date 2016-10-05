from django.conf.urls import patterns, include, url
from .views import CrearItem, ListarItem, DetalleItem, EditItem, DeleteItem

urlpatterns = patterns('',
	url(r'^crear_item/', CrearItem.as_view(), name='crear_item'),
	url(r'^listar_item/', ListarItem.as_view(), name='listar_item'),
	url(r'^detalle_item/(?P<pk>\d+)$', DetalleItem.as_view(), name='detalle_item'),
	url(r'^editar_item/(?P<pk>\d+)$', EditItem.as_view(), name='editar_item'),
	# url(r'^delete_item/(?P<pk>\d+)$', DeleteItem.as_view(), name='delete_item'),
	url(r'^delete_item/(?P<id>\d+)$', 'apps.producto.views.eliminar', name='delete'),

    url(r'^producto_import/', 'apps.producto.views.import_data', name="import_producto"),
    url(r'^configalmacen/', 'apps.producto.views.configalmacen', name="configalmacen"),

)

