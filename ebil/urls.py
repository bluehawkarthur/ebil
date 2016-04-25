"""ebil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.inicio.urls')),
    url(r'^', include('apps.proveedores.urls')),
    # url(r'^', include('apps.almacenes.urls')),
    url(r'^', include('apps.producto.urls')),
    url(r'^', include('apps.cliente.urls')),
    url(r'^', include('apps.compras.urls')),
    url(r'^', include('apps.ventas.urls')),
    url(r'^', include('apps.reportes.urls')),
    url(r'^', include('apps.config.urls')),
    url(r'^', include('apps.bancarizacion.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url for debug toolbar for local and not produccion
    # url(r'^__debug__/', include(debug_toolbar.urls)),
    # url(r'^', include('apps.almacen.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
