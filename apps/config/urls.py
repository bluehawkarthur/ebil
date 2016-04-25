from django.conf.urls import include, url
from .views import ListarPersonajuridica, EditPersonajuridica, DetallePersonajuridica, DeletePersonajuridica, Configuraciones, ListarDatosDosificacion, DetalleDatosDosificacion, EditDatosDosificacion, EditAlmacenesCampos, EditProveedoresCampos, EditClienteCampos, EditFacturaCampos, ListarSucursal, EditSucursal, DetalleSucursal, ListarActividad, EditActividad, DetalleActividad

# import debug_toolbar
urlpatterns = [
    url(r'^createpersojuridica/$', 'apps.config.views.Createpersojuridica', name='createpersojuridica'),
    url(r'^empresa/$', 'apps.config.views.Empresa', name='empresa'),
    url(r'^formato_factura/$', 'apps.config.views.Formatfactura', name='formato_factura'),
    url(r'^editpersonajurid/(?P<pk>\d+)$', 'apps.config.views.EditPersonajuridica', name='editpersonajurid'),
    url(r'^listarPersonajuridica/', ListarPersonajuridica.as_view(), name='listarPersonajuridica'),
    url(r'^edit_Personajuridica/(?P<pk>\d+)$', EditPersonajuridica.as_view(), name='edit_Personajuridica'),
    url(r'^detalle_peronajurid/(?P<pk>\d+)$', DetallePersonajuridica.as_view(), name='detalle_peronajurid'),
    url(r'^delete_personajuridica/(?P<personajuridica>\d+)$', 'apps.config.views.DeletePersonajuridica', name='personajuridica_delete'),
    url(r'^config/', Configuraciones.as_view(), name='config'),
    url(r'^creardatosDosificacion/$', 'apps.config.views.CrearDatosDosificacion', name='creardatosDosificacion'),
    url(r'^lista_datosdosificacion/', ListarDatosDosificacion.as_view(), name='lista_datosdosificacion'),
    url(r'^detalle_datosdosificacion/(?P<pk>\d+)$', DetalleDatosDosificacion.as_view(), name='detalle_datosdosificacion'),
    url(r'^edit_datosdosificacion/(?P<pk>\d+)$', EditDatosDosificacion.as_view(), name='edit_datosdosificacion'),
    url(r'^delete_datosdosificacion/(?P<datosdosificacion>\d+)$', 'apps.config.views.DeleteDatosDosificacion', name='datosdosificacion_delete'),
    url(r'^crearFormatofactura/$', 'apps.config.views.CrearFormatofactura', name='crearFormatofactura'),
    url(r'^copia_base/', 'apps.config.views.copiaBase', name='copia_base'),
    url(r'^base_import/', 'apps.config.views.import_base', name="base_import"),
    url(r'^edit_alamacen_campos/$', EditAlmacenesCampos.as_view(), name='edit_alamacen_campos'),
    url(r'^edit_proveedcamps/$', EditProveedoresCampos.as_view(), name='edit_proveedcamps'),
    url(r'^edit_clientcamp/$', EditClienteCampos.as_view(), name='edit_clientcamp'),
    url(r'^edit_factCamp/$', EditFacturaCampos.as_view(), name='edit_factCamp'),
    url(r'^crearSucursal/$', 'apps.config.views.CreateSucursal', name='crearSucursal'),
    url(r'^listarSucursal/', ListarSucursal.as_view(), name='listarSucursal'),
    url(r'^edit_sucursal/(?P<pk>\d+)$', EditSucursal.as_view(), name='edit_sucursal'),
    url(r'^delete_sucursal/(?P<sucursal>\d+)$', 'apps.config.views.DeleteSucursal', name='sucursal_delete'),
    url(r'^detalle_sucursal/(?P<pk>\d+)$', DetalleSucursal.as_view(), name='detalle_sucursal'),
    url(r'^crear_actividad/$', 'apps.config.views.CrearActividad', name='crear_actividad'),
    url(r'^listar_actividad/', ListarActividad.as_view(), name='listar_actividad'),
    url(r'^delete_activadad/(?P<actividad>\d+)$', 'apps.config.views.DeleteActividad', name='actividad_delete'),
    url(r'^edit_actividad/(?P<pk>\d+)$', EditActividad.as_view(), name='edit_actividad'),
    url(r'^detalle_actividad/(?P<pk>\d+)$', DetalleActividad.as_view(), name='detalle_actividad'),
    url(r'^validador', 'apps.config.views.import_validador', name="validador"),

]
