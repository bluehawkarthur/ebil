from django.shortcuts import render_to_response, render
from apps.bancarizacion.models import Bancarizacion
from .forms import BancarizacionForm

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from pure_pagination.mixins import PaginationMixin
# para exportar excel text
from apps.reportes.excel_utils import WriteToExcel
from django.http import HttpResponse
from .excel_bancarizacion import WriteToBancarizacion
from django.template import loader, Context


# Create your views here.
def CrearBancarizacion(request):
	if request.method =='POST':
		form = BancarizacionForm(request.POST)
		if form.is_valid():
			bancarizacion = Bancarizacion(
				compra_fecha = form.cleaned_data['compra_fecha'],
				venta_fecha = form.cleaned_data['venta_fecha'],
				modal_transacc = form.cleaned_data['modal_transacc'],
				nro_d_cta_doc_de_pago = form.cleaned_data['nro_d_cta_doc_de_pago'],
				fecha_fact_due_fec_doc = form.cleaned_data['fecha_fact_due_fec_doc'],
				monto_pagado_en_doc_d_pago = form.cleaned_data['monto_pagado_en_doc_d_pago'],
				tipo_transaccion = form.cleaned_data['tipo_transaccion'],
				monto_acumulado = form.cleaned_data['monto_acumulado'],
				nro_d_fact_due_nro_doc = form.cleaned_data['nro_d_fact_due_nro_doc'],
				nit_entidad_financiera = form.cleaned_data['nit_entidad_financiera'],
				monto_fact_monto_doc = form.cleaned_data['monto_fact_monto_doc'],
				nro_d_docment_pago = form.cleaned_data['nro_d_docment_pago'],
				nro_d_autoriza_de_fect = form.cleaned_data['nro_d_autoriza_de_fect'],
				tipo_d_documet = form.cleaned_data['tipo_d_documet'],
				nit_ci_cliente = form.cleaned_data['nit_ci_cliente'],
				fecha_d_document_pago = form.cleaned_data['fecha_d_document_pago'],
				razon_social_cliente = form.cleaned_data['razon_social_cliente'])
			bancarizacion.save()
			return HttpResponseRedirect(reverse_lazy('listar_Bancarizacion'))
	else:
		form = BancarizacionForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('bancarizacion/crear_bancar.html', variables)


class ListarBancarizacion(PaginationMixin, ListView):
	template_name = 'bancarizacion/listar_Bancarizacion.html'
	paginate_by = 5
	model = Bancarizacion
	context_object_name = 'bancarizacion'


class DetalleBancarizacion(DetailView):
  template_name = 'bancarizacion/detalle_bancarizacion.html'
  model = Bancarizacion
  context_object_name = 'bancarizacion'


class EditBancarizacion(UpdateView):
	template_name = 'bancarizacion/edit_bancarizacion.html'
	model = Bancarizacion
	fields = ['compra_fecha', 'venta_fecha', 'modal_transacc', 'nro_d_cta_doc_de_pago', 'fecha_fact_due_fec_doc', 'monto_pagado_en_doc_d_pago', 'tipo_transaccion', 'monto_acumulado', 'nro_d_fact_due_nro_doc', 
	'nit_entidad_financiera', 'monto_fact_monto_doc', 'nro_d_docment_pago', 'nro_d_autoriza_de_fect', 'tipo_d_documet', 'nit_ci_cliente', 'fecha_d_document_pago', 'razon_social_cliente']
	success_url = reverse_lazy('listar_Bancarizacion')	
 

def DeleteBancarizacion(request, bancarizacion):
	e = Bancarizacion.objects.get(id= bancarizacion)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('listar_Bancarizacion'))	


def Libro_Bancarizacion(request):
    template_name = "bancarizacion/libro_bancar.html"
    town = None

    if request.method == 'POST':   

	    	bancarizacion = Bancarizacion.objects.all()
	    	total = 0
	    	mes = 0

	        if 'excel' in request.POST:
	            response = HttpResponse(content_type='application/vnd.ms-excel')
	            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	            xlsx_data = WriteToBancarizacion(bancarizacion, mes, total, town)
	            response.write(xlsx_data)
	            return response

	        if 'pdf' in request.POST:
	            response = HttpResponse(content_type='application/pdf')
	            today = date.today()
	            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
	            response['Content-Disposition'] =\
	                'attachement; filename={0}.pdf'.format(filename)
	            buffer = BytesIO()
	            report = Pdfbancarizacion(buffer, 'A4')
	            pdf = report.report(bancarizacion, 'REPORTE DE Bancarizacion', total, mes)
	            response.write(pdf)
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
    return render(request, template_name)   