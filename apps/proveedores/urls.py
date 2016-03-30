from django.conf.urls import include, url
from .views import CrearProveedor, ListProveedor, EditView, ProveedorDelete, ProveedorDetail


urlpatterns = [
    url(r'^crear_proveedor/', CrearProveedor.as_view(), name="crear"),
    url(r'^list_proveedor/', ListProveedor.as_view(), name="lista"),
    url(r'^edit_proveedor/(?P<pk>\d+)$', EditView.as_view(), name='proveedor_edit'),
    # url(r'^delete_proveedor/(?P<pk>\d+)$', ProveedorDelete.as_view(), name='proveedor_delete'),
    url(r'^detail_proveedor/(?P<pk>\d+)$', ProveedorDetail.as_view(), name='proveedor_detail'),
    url(r'^delete_proveedor/(?P<id>\d+)$', 'apps.proveedores.views.eliminar', name='delete'),
    # url(r'^registro_proveedor/', RegistroProveedor.as_view(), name="registro"),
    url(r'^proveedor_import/', 'apps.proveedores.views.import_data', name="import_proveedor"),
    url(r'^configproveedorcampos/', 'apps.proveedores.views.configproveedorcampos', name="configproveedorcampos"),

    
]