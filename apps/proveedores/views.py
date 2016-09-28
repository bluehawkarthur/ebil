from django.shortcuts import render
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .forms import CreateForm
from .models import Proveedor
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponseRedirect 
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
import django_excel as excel
from django.contrib import messages
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import sys
from django.db import IntegrityError
PY2 = sys.version_info[0] == 2
if PY2:
    import pyexcel.ext.ods
else:
    import pyexcel.ext.ods3

from django.http import HttpResponse
import json
from apps.config.models import ProveedoresCampos
from django.core import serializers


def configproveedorcampos(request):
    config = ProveedoresCampos.objects.filter(empresa=request.user.empresa)
    data = serializers.serialize(
        'json', config, fields=('direccion_usar', 'direccion_requerido', 'direccion_tipo', 'direccion_caractr',
	'telefonos1_usar', 'telefonos1_requerido', 'telefonos1_tipo', 'telefonos1_caractr', 'telefonos2_usar', 'telefonos2_requerido', 'telefonos2_tipo', 'telefonos2_caractr',
	'telefonos3_usar', 'telefonos3_requerido', 'telefonos3_tipo', 'telefonos3_caractr', 'contacto_usar', 'contacto_requerido', 'contacto_tipo', 'contacto_caractr', 
	'rubro_usar', 'rubro_requerido', 'rubro_tipo', 'rubro_caractr', 'ubicacion_geo_usar', 'ubicacion_geo_requerido', 'ubicacion_geo_tipo', 'ubicacion_geo_caractr', 
	'fechas_usar', 'fechas_requerido', 'fechas2_usar', 'fechas2_requerido', 'textos_usar', 'textos_requerido', 'textos_tipo', 'textos_caractr',
	'textos2_usar', 'textos2_requerido', 'textos2_tipo', 'textos2_caractr'))
    return HttpResponse(data, content_type="application/json")


# Create your views here.
class CrearProveedor(SuccessMessageMixin, FormView):
	template_name = "proveedores/create.html"
	form_class = CreateForm
	success_url = reverse_lazy('lista')
	success_message = "%(razon_social)s fue creado con exito"

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
		registrar.empresa = self.request.user.empresa
		try:
			registrar.save()
		except IntegrityError:
			messages.error(self.request, "error CODIGO DUPLICADO")
			return self.form_invalid(form)
		
		

		return super(CrearProveedor, self).form_valid(form)

	

class ListProveedor(PaginationMixin, ListView):
	template_name = "proveedores/lista.html"
	model = Proveedor
	paginate_by = 5
	
	def get_queryset(self):

		razon_social = self.request.GET.get('q', None)
		    
		if (razon_social):
		    object_list = self.model.objects.filter(razon_social__icontains=razon_social, empresa=self.request.user.empresa).order_by('pk')
		else:
		    object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('pk')
		return object_list



class EditView(UpdateView):
    template_name = 'proveedores/update.html'
    model = Proveedor
    fields = ['codigo', 'razon_social', 'nit', 'direccion','telefono1', 'telefono2', 'telefono3', 'contactos'
    , 'rubro', 'ubicacion_geo', 'fecha1', 'fecha2', 'texto1', 'texto2']
    success_url = reverse_lazy('lista')

    def get_form(self, form_class):
        form = super(EditView, self).get_form(form_class)
        form.fields['telefono2'].required=False
        return form

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
            request.FILES['file'].save_book_to_database(
                models=[Proveedor],
                initializers=[choice_func],
                mapdicts=[['codigo', 'razon_social', 'nit','direccion', 'telefono1', 'contactos', 'rubro', 'ubicacion_geo', 'fecha1', 'fecha2', 'texto1', 'texto2', 'empresa']]
            )
            return HttpResponseRedirect(reverse_lazy('lista'))
        
    else:
        form = UploadFileForm()
    return render_to_response(
        'proveedores/upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        },
        context_instance=RequestContext(request))
