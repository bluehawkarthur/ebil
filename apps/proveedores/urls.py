from django.conf.urls import include, url
from .views import CrearProveedor

urlpatterns = [
    url(r'^crear_proveedor/', CrearProveedor.as_view(), name="crear"),
    
]