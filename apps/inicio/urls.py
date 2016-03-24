from django.conf.urls import include, url

from .views import LoginView, LogoutView, Index, Inicio, Reportes, ListarUsuario, EditUser, InicioRoot

urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
  	url(r'^logout/$', LogoutView.as_view(), name='logout'),
  	url(r'^inicio/$', Inicio.as_view(), name='inicio'),
    url(r'^inicio_root/$', InicioRoot.as_view(), name='inicio_root'),
  	url(r'^reportes/$', Reportes.as_view(), name='reportes'),
  	url(r'^register/$', 'apps.inicio.views.register', name='register'),
  	url(r'^list_user/$', ListarUsuario.as_view(), name='list_user'),
  	url(r'^delete_user/(?P<id>\d+)$', 'apps.inicio.views.eliminar', name='delete_user'),
  	url(r'^editar_user/(?P<pk>\d+)$', 'apps.inicio.views.user_edit', name='editar_user'),
  	url(r'^editar_user/(?P<pk>\d+)/password$', 'apps.inicio.views.change_password', name='user_password'),
    url(r'^permisos_user/(?P<pk>\d+)$', 'apps.inicio.views.user_permisos', name='permisos_user'),
    url(r'^perfil/$', 'apps.inicio.views.perfil', name='perfil'),
  	
]
