from django.conf.urls import include, url

from .views import LoginView, LogoutView, Index, Inicio, Reportes

urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
  	url(r'^logout/$', LogoutView.as_view(), name='logout'),
  	url(r'^inicio/$', Inicio.as_view(), name='inicio'),
  	url(r'^reportes/$', Reportes.as_view(), name='reportes'),

  	
]
