from django.conf.urls import url
from .views import Success

urlpatterns = [
    url(r'^recetas/registrar/$', 'apps.compras.views.registro_edicion', name='registrar'),
    url(r'^recetas/(?P<receta_id>\d+)/$', 'apps.compras.views.registro_edicion', name='editar'),
    url(r'^success/$', Success.as_view(), name='success'),
    url(r'^buscar_item/$', 'apps.compras.views.buscarProducto'),
]
