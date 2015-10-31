# views.py
from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import Compra, DetalleCompra
from .forms import CompraForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseBadRequest,HttpResponse
from django.core import serializers
import json
from apps.producto.models import Item



def registro_edicion(request, receta_id=None):
    if receta_id:
        receta = Compra.objects.get(pk=receta_id)
    else:
        receta = Compra()

    IngredienteFormSet = inlineformset_factory(Compra, DetalleCompra, extra=10, can_delete=True, exclude={'producto'})
  

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=receta)
        ingredienteFormset = IngredienteFormSet(request.POST, instance=receta)

        if form.is_valid() and ingredienteFormset.is_valid():
            form.save()
            print ingredienteFormset
            ingredienteFormset.save()
            return HttpResponseRedirect(reverse_lazy('success'))

    else:
        form = CompraForm(instance=receta)
        ingredienteFormset = IngredienteFormSet(instance=receta)

    return render('compras/compra.html', locals(),
        context_instance=ctx(request))

class Success(TemplateView):
	template_name='compras/success.html'


def buscarProducto(request):
    idProducto = request.GET['id']
    producto = Item.objects.filter(descripcion__contains=idProducto)
    data = serializers.serialize(
        'json', producto, fields=('codigo_item','codigo_fabrica', 'descripcion', 'precio_unitario', 'unidad_medida'))
    return HttpResponse(data, content_type='application/json')