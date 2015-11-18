from django.shortcuts import render
from .forms import ClienteForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Cliente
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
class CrearCliente(FormView):
	template_name = 'cliente/crear_Cliente.html'
	form_class = ClienteForm
	success_url = reverse_lazy('listar_cliente')
	success_message = "%(razon_social)s fue creado con exito"


	def form_valid(self, form):
		cliente = Cliente()
		cliente.codigo = form.cleaned_data['codigo']
		cliente.razonsocial = form.cleaned_data['razonsocial']
		cliente.nit = form.cleaned_data['nit']
		cliente.direccion = form.cleaned_data['direccion']
		cliente.telefonos1 = form.cleaned_data['telefonos1']
		cliente.telefonos2 = form.cleaned_data['telefonos2']
		cliente.telefonos3 = form.cleaned_data['telefonos3']
		cliente.contacto = form.cleaned_data['contacto']
		cliente.rubro = form.cleaned_data['rubro']
		cliente.categoria = form.cleaned_data['categoria']
		cliente.ubucaciongeo = form.cleaned_data['ubucaciongeo'] 
		cliente.fecha = form.cleaned_data['fecha']
		cliente.fecha2 = form.cleaned_data['fecha2']
		cliente.textos = form.cleaned_data['textos']
		cliente.textos2 = form.cleaned_data['textos2']
		cliente.save()
		messages.success(self.request, 'El cliente se a guardado correctamente')
		return super(CrearCliente, self).form_valid(form)


class ListarCliente(ListView):
	template_name = 'cliente/listar_cliente.html'
	model = Cliente
	context_object_name = 'cliente'	

class DetalleCliente(DetailView):
	template_name = 'cliente/detalle_cliente.html'
	model = Cliente
	context_object_name = 'Cliente'


class EditCliente(UpdateView):
    template_name = 'cliente/update.html'
    model = Cliente
    fields = ['codigo','razonsocial', 'nit', 'direccion', 'telefonos1', 'telefonos2', 'telefonos3'
    , 'contacto', 'rubro', 'categoria', 'ubucaciongeo', 'fecha', 'fecha2', 'textos', 'textos2']
    success_url = reverse_lazy('listar_cliente')


def eliminar(request, id):
	p = Cliente.objects.get(id=id)
	p.delete()
	messages.success(request, 'El cliente se elimino correctamente')
	print p 
	return HttpResponseRedirect(reverse_lazy('listar_cliente'))