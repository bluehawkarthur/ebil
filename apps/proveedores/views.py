from django.shortcuts import render
from django.views.generic import CreateView,FormView
from .forms import CreateForm
from .models import Proveedor
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CrearProveedor(FormView):
	template_name = "proveedores/create.html"
	form_class = CreateForm
	succes_url = reverse_lazy('crear')

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
	
		
