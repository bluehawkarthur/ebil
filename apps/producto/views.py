from django.shortcuts import render
from .forms import ItemForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Item
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponseRedirect
from django import forms
from .models import Proveedor


class CrearItem(FormView):
	template_name = 'producto/crear_item.html'
	form_class = ItemForm
	success_url = reverse_lazy('listar_item')

	# personalize choices for user authenticate
	def get_form(self, form_class):
		form = form_class(**self.get_form_kwargs())
		form.fields['proveedor'].queryset = Proveedor.objects.filter(user=self.request.user.id).all()
		return form

	def form_valid(self, form):
			item = Item()
			item.codigo_item = form.cleaned_data['codigo_item']
			item.codigo_fabrica = form.cleaned_data['codigo_fabrica']
			item.almacen = form.cleaned_data['almacen']
			item.grupo = form.cleaned_data['grupo']
			item.subgrupo = form.cleaned_data['subgrupo']
			item.descripcion = form.cleaned_data['descripcion']
			item.carac_especial_1 = form.cleaned_data['carac_especial_1']
			item.carac_especial_2 = form.cleaned_data['carac_especial_2']
			item.cantidad = form.cleaned_data['cantidad']
			item.saldo_min = form.cleaned_data['saldo_min']
			item.proveedor = form.cleaned_data['proveedor']
			item.imagen = form.cleaned_data['imagen']
			item.unidad_medida = form.cleaned_data['unidad_medida']
			item.costo_unitario = form.cleaned_data['costo_unitario']
			item.precio_unitario = form.cleaned_data['precio_unitario']
			item.user= self.request.user
			item.save()
			return super(CrearItem, self).form_valid(form)




class ListarItem(PaginationMixin, ListView):
	template_name = 'producto/listar_item.html'
	model = Item
	paginate_by = 3
	context_object_name = 'item'


class DetalleItem(DetailView):
	template_name = 'producto/detalle_item.html'
	model = Item
	context_object_name = 'item'


class EditItem(UpdateView):
    template_name = 'producto/update.html'
    model = Item
    fields = ['codigo_item','codigo_fabrica','almacen','grupo','subgrupo',
    'descripcion','carac_especial_1','carac_especial_2','cantidad',
    'saldo_min','proveedor','imagen','unidad_medida','costo_unitario','precio_unitario']
    success_url = reverse_lazy('listar_item')


class DeleteItem(DeleteView):
	model = Item
	success_url = reverse_lazy('listar_item')


def eliminar(request, id):
	p = Item.objects.get(id=id)
	p.delete()
	return HttpResponseRedirect(reverse_lazy('listar_item'))