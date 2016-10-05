# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import ClienteForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Cliente
from django.http import HttpResponseRedirect
from django.contrib import messages
from pure_pagination.mixins import PaginationMixin
#De excel
import django_excel as excel
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel as pe
import sys
PY2 = sys.version_info[0] == 2
if PY2:
    import pyexcel.ext.ods
else:
    import pyexcel.ext.ods3

from ebil.settings import MEDIA_ROOT

import os
import xlrd
from datetime import date

IMPORT_FILE_TYPES = ['.xls', '.xlsx', ]
from django import forms
from django.template import RequestContext

# personalize de configuracions de cliente y ciente campos  validacion
from apps.config.models import ClienteCampos
from django.http import HttpResponse
import json
from django.core import serializers


# personalize de configuracions de cliente y ciente campos 
def configclient(request):
    config = ClienteCampos.objects.filter(empresa=request.user.empresa)
    data = serializers.serialize(
        'json', config, fields=('direccion_usar', 'direccion_requerido','direccion_tipo', 'direccion_caractr', 
  'telefono1_usar', 'telefono1_requerido', 'telefono1_tipo', 'telefono1_caractr', 'telefono2_usar', 'telefono2_requerido', 'telefono2_tipo', 'telefono2_caractr', 
  'telefono3_usar', 'telefono3_requerido', 'telefono3_tipo', 'telefono3_caractr', 'contacto_usar', 'contacto_requerido', 'contacto_tipo', 'contacto_caractr', 
  'rubro_usar', 'rubro_requerido', 'rubro_tipo', 'rubro_caractr', 'categoria_usar', 'categoria_requerido', 'categoria_tipo', 'categoria_caractr', 
  'ubicaciongeo_usar', 'ubicaciongeo_requerido', 'ubicaciongeo_tipo', 'ubicaciongeo_caractr', 'fecha_usar', 'fecha_requerido', 'fecha2_usar', 'fecha2_requerido',
  'texto_usar', 'texto_requerido', 'texto_tipo', 'texto_caractr', 'texto2_usar', 'texto2_requerido', 'texto2_tipo', 'texto2_caractr'))
    return HttpResponse(data, content_type="application/json")


# Create your views here.
class CrearCliente(FormView):
	template_name = 'cliente/crear_Cliente.html'
	form_class = ClienteForm
	success_url = reverse_lazy('listar_cliente')
	success_message = "%(razon_social)s fue creado con exito"

	def get_form_kwargs(self):
		kwargs = super(CrearCliente, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

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
		cliente.empresa = self.request.user.empresa
		cliente.save()
		messages.success(self.request, 'El cliente se a guardado correctamente')
		return super(CrearCliente, self).form_valid(form)


class ListarCliente(PaginationMixin, ListView):
	template_name = 'cliente/listar_cliente.html'
	model = Cliente
	context_object_name = 'cliente'
	paginate_by = 5

	def get_queryset(self):

		razon_social = self.request.GET.get('q', None)
		    
		if (razon_social):
		    object_list = self.model.objects.filter(razonsocial__icontains=razon_social, empresa=self.request.user.empresa).order_by('razonsocial')
		else:
		    object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('razonsocial')
		return object_list


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


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean(self):
      data = super(UploadFileForm, self).clean()

      if 'file' not in data:
          raise forms.ValidationError('')
          docfile = data['file']
      extension = os.path.splitext(docfile.name)[1]

      if not (extension in IMPORT_FILE_TYPES):
          raise forms.ValidationError(u'%s no es un archivo válido. Por favor, asegurese de que su archivo de entrada tenga la extension .xls' % docfile.name)



#====== views for import archivo of excel ======
class UploadFileForm(forms.Form):
    file = forms.FileField()


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        def choice_func(row):
            row.append(request.user.empresa)
            return row

        if form.is_valid():
        	try:
	            request.FILES['file'].save_book_to_database(
	                models=[Cliente],
	                initializers=[choice_func],
	                mapdicts=[['codigo', 'razonsocial', 'nit', 'direccion', 'telefonos1', 'telefonos2', 'telefonos3', 'contacto', 'rubro', 'categoria', 'ubucaciongeo', 'fecha', 'fecha2', 'textos', 'textos2','empresa']]
	            )
	            return HttpResponseRedirect(reverse_lazy('lista'))
	        except Exception, e:
	        	messages.error(request, "error en el archivo por favor verifique q los datos sean correctos")
    else:
        form = UploadFileForm()
    return render_to_response(
        'cliente/upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        },
        context_instance=RequestContext(request))