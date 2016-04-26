from django.shortcuts import render_to_response, render
from apps.bancarizacion.models import BancarizacionCompras, BancarizacionVentas
from .forms import BancarizacionComprasForm, BancarizacionVentasForm

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from pure_pagination.mixins import PaginationMixin
# para exportar excel text
from apps.reportes.excel_utils import WriteToExcel
from django.http import HttpResponse
from .excel_bancarizacion import WriteToBancarizacionCompras
from .excel_bancar_venta import WriteToBancarizacionVentas
from django.template import loader, Context
from django.contrib import messages


# Create your views here.
def CrearBancarizacionCompras(request):
	if request.method == 'POST':
		form = BancarizacionComprasForm(request.POST)
		if form.is_valid():
			bancarizacion = BancarizacionCompras(
				compra_fecha=form.cleaned_data['compra_fecha'],
				modalidad_d_la_transaccion=form.cleaned_data['modalidad_d_la_transaccion'],
				nro_de_cta_doc_de_pago=form.cleaned_data['nro_de_cta_doc_de_pago'],
				fecha_fact_dui_fecha_doc=form.cleaned_data['fecha_fact_dui_fecha_doc'],
				monto_pagado_en_doc_d_pago=form.cleaned_data['monto_pagado_en_doc_d_pago'],
				tipo_transaccion=form.cleaned_data['tipo_transaccion'],
				monto_acumulado=form.cleaned_data['monto_acumulado'],
				nit_proveedor=form.cleaned_data['nit_proveedor'],
				nit_entidad_inanciera=form.cleaned_data['nit_entidad_inanciera'],
				razon_social_proveedor=form.cleaned_data['razon_social_proveedor'],
				nro_d_documento_de_pago=form.cleaned_data['nro_d_documento_de_pago'],
				nro_d_fact_dui_nro_doc=form.cleaned_data['nro_d_fact_dui_nro_doc'],
				tipo_de_doc_d_pago=form.cleaned_data['tipo_de_doc_d_pago'],
				tipo_de_documento=form.cleaned_data['tipo_de_documento'],
				monto_fact_monto_dui_monto_doc=form.cleaned_data['monto_fact_monto_dui_monto_doc'],
				fecha_d_documento_d_pago=form.cleaned_data['fecha_d_documento_d_pago'],
				nro_de_aut_fact_dui_documento=form.cleaned_data['nro_de_aut_fact_dui_documento'],
				empresa=request.user.empresa)
			bancarizacion.save()
			return HttpResponseRedirect(reverse_lazy('listar_Bancarizacion'))
	else:
		form = BancarizacionComprasForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('bancarizacion/crear_bancar.html', variables)


class ListarBancarizacionCompras(PaginationMixin, ListView):
	template_name = 'bancarizacion/listar_Bancarizacion.html'
	paginate_by = 5
	model = BancarizacionCompras
	context_object_name = 'bancarizacion'

	def get_queryset(self):
		object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('pk')
		return object_list


class DetalleBancarizacionCompras(DetailView):
  template_name = 'bancarizacion/detalle_bancarizacion.html'
  model = BancarizacionCompras
  context_object_name = 'bancarizacion'


class EditBancarizacionCompras(UpdateView):
	template_name = 'bancarizacion/edit_bancarizacion.html'
	model = BancarizacionCompras
	form_class = BancarizacionComprasForm

	success_url = reverse_lazy('listar_Bancarizacion')
 

def DeleteBancarizacionCompras(request, bancarizacion):
	e = BancarizacionCompras.objects.get(id= bancarizacion)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('listar_Bancarizacion'))


def Libro_BancarizacionCompras(request):
    template_name = "bancarizacion/libro_bancar.html"
    town = None

    if request.method == 'POST':

    	bancarizacion = BancarizacionCompras.objects.filter(empresa=request.user.empresa)
    	total = 0
    	mes = 0

    	try:
	        if 'excel' in request.POST:
	            response = HttpResponse(content_type='application/vnd.ms-excel')
	            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	            xlsx_data = WriteToBancarizacionCompras(bancarizacion, mes, total, town)
	            response.write(xlsx_data)
	            return response

	        if 'txt' in request.POST:
	            response = HttpResponse(content_type='text/plain; charset=utf-8')
	            response['Content-Disposition'] = 'attachment; filename="output_bancarizacion.txt"'
	            t = loader.get_template('bancarizacion/bancari.txt')

	            c = Context({'bancarizacion' : bancarizacion, })

	            response.write(t.render(c))
	            return response

	    	context = {
		        'town': town,
		        'bancarizacion': bancarizacion,
		    }

	        return render(request, template_name, context)

        except Exception, e:
    		messages.error(request, 'No existen datos')
    return render(request, template_name)


def CrearBancarizacionVentas(request):
	if request.method =='POST':
		form = BancarizacionVentasForm(request.POST)
		if form.is_valid():
			bancariventas = BancarizacionVentas(
				venta_fecha = form.cleaned_data['venta_fecha'],
				modalidad_d_la_transaccion = form.cleaned_data['modalidad_d_la_transaccion'],
				nro_de_cta_doc_de_pago = form.cleaned_data['nro_de_cta_doc_de_pago'],
				fecha_fact_dui_fecha_doc = form.cleaned_data['fecha_fact_dui_fecha_doc'],
				monto_pagado_en_doc_d_pago = form.cleaned_data['monto_pagado_en_doc_d_pago'],
				tipo_transaccion = form.cleaned_data['tipo_transaccion'],
				monto_acumulado = form.cleaned_data['monto_acumulado'],
				nro_d_fact_dui_nro_doc = form.cleaned_data['nro_d_fact_dui_nro_doc'],
				nit_entidad_inanciera = form.cleaned_data['nit_entidad_inanciera'],
				monto_fact_monto_doc = form.cleaned_data['monto_fact_monto_doc'],
				nro_d_documento_de_pago = form.cleaned_data['nro_d_documento_de_pago'],
				nro_de_auturizacion_d_fact = form.cleaned_data['nro_de_auturizacion_d_fact'],
				tipo_de_doc_d_pago = form.cleaned_data['tipo_de_doc_d_pago'],
				tipo_de_documento = form.cleaned_data['tipo_de_documento'],
				nit_ci_d_cliente = form.cleaned_data['nit_ci_d_cliente'],
				fecha_d_documento_d_pago = form.cleaned_data['fecha_d_documento_d_pago'],
				razon_social_cliente = form.cleaned_data['razon_social_cliente'],
				empresa=request.user.empresa)
			bancariventas.save()
			return HttpResponseRedirect(reverse_lazy('listar_Bancar_ventas'))
	else:
		form = BancarizacionVentasForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('bancarizacion/crear_bancar_ventas.html', variables)


class ListarBancarizacionVentas(PaginationMixin, ListView):
	template_name = 'bancarizacion/listar_Bancar_ventas.html'
	paginate_by = 5
	model = BancarizacionVentas
	context_object_name = 'bancar_venat'

	def get_queryset(self):
		object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('pk')
		return object_list


class DetalleBancarizacionVentas(DetailView):
  template_name = 'bancarizacion/detalle_Bancar_ventas.html'
  model = BancarizacionVentas
  context_object_name = 'bancar_venat'

class EditBancarizacionVentas(UpdateView):
	template_name = 'bancarizacion/edit_Bancar_ventas.html'
	model = BancarizacionVentas
	fields = ['venta_fecha', 'modalidad_d_la_transaccion', 'nro_de_cta_doc_de_pago', 'fecha_fact_dui_fecha_doc', 'monto_pagado_en_doc_d_pago',
		'tipo_transaccion', 'monto_acumulado', 'nro_d_fact_dui_nro_doc', 'nit_entidad_inanciera', 'monto_fact_monto_doc', 'nro_d_documento_de_pago',
		'nro_de_auturizacion_d_fact', 'tipo_de_doc_d_pago', 'tipo_de_documento', 'nit_ci_d_cliente', 'fecha_d_documento_d_pago', 'razon_social_cliente']
	success_url = reverse_lazy('listar_Bancar_ventas')


def DeleteBancarizacionVentas(request, bancarizacion):
	e = BancarizacionVentas.objects.get(id= bancarizacion)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('listar_Bancar_ventas'))


def Libro_BancarizacionVentas(request):
    template_name = "bancarizacion/libro_bancar_venta.html"
    town = None

    if request.method == 'POST':

    	bancarizacion = BancarizacionVentas.objects.filter(empresa=request.user.empresa)
    	total = 0
    	mes = 0
    	try:
    	
	        if 'excel' in request.POST:
	            response = HttpResponse(content_type='application/vnd.ms-excel')
	            response['Content-Disposition'] = 'attachment; filename=bancariventas.xlsx'
	            xlsx_data = WriteToBancarizacionVentas(bancarizacion, mes, total, town)
	            response.write(xlsx_data)
	            return response

	        if 'txt' in request.POST:
	            response = HttpResponse(content_type='text/plain; charset=utf-8')
	            response['Content-Disposition'] = 'attachment; filename="bancariventas.txt"'
	            t = loader.get_template('bancarizacion/bancar_venta.txt')

	            c = Context({'bancarizacion' : bancarizacion, })

	            response.write(t.render(c))
	            return response

	    	context = {
		        'town': town,
		        'bancarizacion': bancarizacion,
		    }

	        return render(request, template_name, context)
        
        except Exception, e:
        	messages.error(request, 'No existen datos')

    return render(request, template_name)
