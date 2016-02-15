from django.conf.urls import include, url
from .views import ListarPersonajuridica, EditPersonajuridica, DetallePersonajuridica, DeletePersonajuridica, Configuraciones, ListarDatosDosificacion, DetalleDatosDosificacion, EditDatosDosificacion

# import debug_toolbar
urlpatterns = [
    url(r'^createpersojuridica/$', 'apps.config.views.Createpersojuridica', name='createpersojuridica'),
    url(r'^empresa/$', 'apps.config.views.Empresa', name='empresa'),
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


]