from django.shortcuts import render
from .forms import ClienteForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Cliente
# Create your views here.
class CrearCliente(FormView):
	template_name = 'cliente/crear_Cliente.html'
	form_class = ClienteForm
	success_url = reverse_lazy('listar_cliente')

	def form_valid(self, form):
		cliente = Cliente()
		cliente.codigo = form.cleaned_data['codigo']
		cliente.razonSocial = form.cleaned_data['razonSocial']
		cliente.nit = form.cleaned_data['nit']
		cliente.Direccion = form.cleaned_data['Direccion']
		cliente.telefonos1 = form.cleaned_data['telefonos1']
		cliente.telefonos2 = form.cleaned_data['telefonos2']
		cliente.telefonos3 = form.cleaned_data['telefonos3']
		cliente.contacto = form.cleaned_data['contacto']
		cliente.rubro = form.cleaned_data['rubro']
		cliente.categoria = form.cleaned_data['categoria']
		cliente.UbucacionGeo = form.cleaned_data['UbucacionGeo'] 
		cliente.fecha = form.cleaned_data['fecha']
		cliente.fecha2 = form.cleaned_data['fecha2']
		cliente.textos = form.cleaned_data['textos']
		cliente.textos2 = form.cleaned_data['textos2']
		cliente.save()
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
    success_url = reverse_lazy('elimanar_cliente')


class DeleteCliente(DeleteView):
	model = Cliente
	success_url = reverse_lazy('listar_cliente')	