from django.conf.urls import patterns, include, url
from .views import CrearItem

urlpatterns = patterns('',
	url(r'^crear_item/', CrearItem.as_view(), name='crear_item'),
)
