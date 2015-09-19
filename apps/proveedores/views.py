from django.shortcuts import render
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .forms import CreateForm
from .models import Proveedor
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponseRedirect 

# Create your views here.
class CrearProveedor(SuccessMessageMixin, FormView):
	template_name = "proveedores/create.html"
	form_class = CreateForm
	success_url = reverse_lazy('lista')
	success_message = "%(razon_social)s was created successfully"


	def form_valid(self, form):
		registrar = Proveedor()
		registrar.codigo = form.cleaned_data['codigo']
		registrar.razon_social = form.cleaned_data['razon_social']
		registrar.nit = form.cleaned_data['nit']
		registrar.direccion = form.cleaned_data['direccion'] 
		registrar.telefono1 = form.cleaned_data['telefono1']
		registrar.telefono2 = form.cleaned_data['telefono2']
		registrar.telefono3 = form.cleaned_data['telefono3']
		registrar.contactos = form.cleaned_data['contactos']
		registrar.rubro = form.cleaned_data['rubro']
		registrar.ubicacion_geo = form.cleaned_data['ubicacion_geo']
		registrar.fecha1 = form.cleaned_data['fecha1']
		registrar.fecha2 = form.cleaned_data['fecha2']
		registrar.texto1 = form.cleaned_data['texto1']
		registrar.fecha2 = form.cleaned_data['fecha2']
		registrar.save()
		return super(CrearProveedor, self).form_valid(form)
	

class ListProveedor(PaginationMixin, ListView):
	template_name = "proveedores/lista.html"
	model = Proveedor
	paginate_by = 3
	queryset = Proveedor.objects.all().order_by('pk')

class EditView(UpdateView):
    template_name = 'proveedores/update.html'
    model = Proveedor
    fields = ['codigo','razon_social','nit','direccion','telefono1','telefono2','telefono3','contactos'
    ,'rubro','ubicacion_geo','fecha1','fecha2','texto1','texto2']
    success_url = reverse_lazy('lista')

class ProveedorDelete(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('lista')

class ProveedorDetail(DetailView):
	template_name = 'proveedores/detail.html'
	model = Proveedor
	success_url = reverse_lazy('lista')

def eliminar(request, id):
	p = Proveedor.objects.get(id=id)
	p.delete()
	print p 
	return HttpResponseRedirect(reverse_lazy('lista'))