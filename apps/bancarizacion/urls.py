from django.conf.urls import include, url
from .views import ListarBancarizacion, DetalleBancarizacion, EditBancarizacion, DeleteBancarizacion


# import debug_toolbar
urlpatterns = [
    url(r'^crear_bancar/$', 'apps.bancarizacion.views.CrearBancarizacion', name='crear_bancar'),
    url(r'^listar_Bancarizacion/', ListarBancarizacion.as_view(), name='listar_Bancarizacion'),
    url(r'^detalle_bancarizacion/(?P<pk>\d+)$', DetalleBancarizacion.as_view(), name='detalle_bancarizacion'),
    url(r'^edit_bancarizacion/(?P<pk>\d+)$', EditBancarizacion.as_view(), name='edit_bancarizacion'),
    url(r'^delete_bancarizacion/(?P<bancarizacion>\d+)$', 'apps.bancarizacion.views.DeleteBancarizacion', name='bancarizacion_delete'),
    url(r'^libro_bancar/', 'apps.bancarizacion.views.Libro_Bancarizacion', name='libro_bancar'),
]