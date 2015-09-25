from django.shortcuts import render
from .forms import ItemForm
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .models import Item

class CrearItem(FormView):
	template_name = 'almacenes/crear_item.html'
	form_class = ItemForm
	success_url = reverse_lazy('crear_item')

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
			item.save()
			return super(CrearItem, self).form_valid(form)




