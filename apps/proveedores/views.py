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
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import sys
PY2 = sys.version_info[0] == 2
if PY2:
    import pyexcel.ext.ods
else:
    import pyexcel.ext.ods3

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
		registrar.user= self.request.user
		registrar.save()
		return super(CrearProveedor, self).form_valid(form)
	

class ListProveedor(PaginationMixin, ListView):
	template_name = "proveedores/lista.html"
	model = Proveedor
	paginate_by = 5
	

	def get_queryset(self):
		queryset = super(ListProveedor, self).get_queryset()
		return Proveedor.objects.filter(user=self.request.user.id).all().order_by('pk')



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


#====== views for import archivo of excel ======
class UploadFileForm(forms.Form):
    file = forms.FileField()


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        def choice_func(row):
            print 'aquiiiiiiii stasssss'
            print row[0]
            
            print 'muestra qqqqq'
   
            row.append(request.user)

            print row
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Proveedor],
                initializers=[choice_func],
                mapdicts=[['codigo', 'razon_social', 'nit','direccion', 'telefono1', 'contactos', 'rubro', 'ubicacion_geo', 'fecha1', 'fecha2', 'texto1', 'texto2', 'user']]
            )
            return HttpResponseRedirect(reverse_lazy('lista'))
        else:
            return HttpResponseBadRequest()
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