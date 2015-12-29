# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from apps.compras.models import Compra, DetalleCompra
from apps.ventas.models import Venta, DetalleVenta
from apps.producto.models import Item
from .htmltopdf import render_to_pdf
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from django.template import RequestContext as ctx
# import xlsxwriter
from .excel_utils import WriteToExcel
from .excel_almacen import WriteToAlmacen
from .excel_compras import WriteToCompras
from .excel_ventas import WriteToVentas
from .pdf_utils import PdfPrint
from .pdf_almacen import PdfAlmacen
from .pdf_compras import PdfCompras
from .pdf_ventas import PdfVentas
import json
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponseBadRequest,HttpResponse
from datetime import date
from django.template import loader, Context
from django.contrib import messages


class RepCompras(TemplateView):
	template_name = 'reportes/rep_compras.html'

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		if buscar != '':
			it = Item.objects.filter(codigo_item=buscar)
			if it:
				v = it[0].cantidad
				detalles = DetalleCompra.objects.filter(producto=it)
				# print 'ESTO ES DETALLES', detalles
				if detalles:
					factura = []
					for detalle in detalles:
						fact  = detalle.compra
						factura.append(dict([(fact, detalle)]))
					return render(request, 'reportes/rep_compras.html', {'factura':factura, 'ex':True, 'v':v})
				else:
					return render(request, 'reportes/rep_compras.html', {'ex':False})
			else: #Si it no existe
				return render(request, 'reportes/rep_compras.html', {'ex':False})
		else: #Si buscar esta vacio
			return render(request, 'reportes/rep_compras.html', {'ex':False})


def buscarProducto(request):

	idProducto = request.GET['id']
	producto = Item.objects.filter(codigo_item__contains=idProducto)
	if producto:
		data = serializers.serialize(
		'json', producto, fields=('codigo_item', 'descripcion',))
	else:
		descripcion = Item.objects.filter(descripcion__contains=idProducto)
		data = serializers.serialize(
		'json', descripcion, fields=('codigo_item', 'descripcion',))
	return HttpResponse(data, content_type='application/json')

def buscarEmpresa(request):

	idEmpresa = request.GET['id']
	producto = Venta.objects.filter(razon_social__contains=idEmpresa)
	if producto:
		data = serializers.serialize(
		'json', producto, fields=('razon_social', 'nit',))
	else:
		nit = Venta.objects.filter(nit__contains=idEmpresa)
		data = serializers.serialize(
		'json', nit, fields=('razon_social', 'nit',))

	return HttpResponse(data, content_type='application/json')
	

class RepVentas(TemplateView):
	template_name = 'reportes/rep_ventas.html'

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		if buscar != '':
			it = Item.objects.filter(codigo_item=buscar)
			if it:
				v = it[0].cantidad
				vv = it[0].descripcion
				detalles = DetalleVenta.objects.filter(codigo=it)
				# print 'ESTO ES DETALLES', detalles
				if detalles:
					factura = []
					for detalle in detalles:
						fact  = detalle.venta
						print fact
						factura.append(dict([(fact, detalle)]))
					return render(request, 'reportes/rep_ventas.html', {'factura':factura, 'ex':True, 'v':v, 'vv':vv})
				else:
					return render(request, 'reportes/rep_ventas.html', {'ex':False})
			else: #Si it no existe
				return render(request, 'reportes/rep_ventas.html', {'ex':False})
		else: #Si buscar esta vacio
			return render(request, 'reportes/rep_ventas.html', {'ex':False})


def Reporteventa(request):
	if request.method == 'POST':
		date1 = request.POST['date1']
		date2 = request.POST['date2']
		tipo = request.POST['tipo_venta']
		nit = request.POST['nit2']
		monto = request.POST['monto2']
		empresa = request.POST['empresa2']
		

		if date1 != '':
			if tipo == 'todo':
				if nit != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), nit=nit)
				elif empresa != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), razon_social=empresa)
				elif monto != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), total__gte=monto)
				else:
					ventas = Venta.objects.filter(fecha__range=(date1, date2))
			else:
				if nit != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, nit=nit)
				elif empresa != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, razon_social=empresa)
				elif monto != '':
					ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, total__gte=monto)
				else:
					ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo)
			
			total = 0
			for venta in ventas:
				total += venta.total
			
			return render(request, 'reportes/reporte_venta.html', {'ventas':ventas, 'total':total, 'ex':True, 'date1': date1, 'date2': date2})
		
	else:
		datecompu = date.today()
		total = 0
		ventas = Venta.objects.filter(fecha=datecompu)
		for venta in ventas:
			total += venta.total

		return render(request, 'reportes/reporte_venta.html', {'ventas':ventas, 'total':total, 'ex':True})
# class ReportVendetalle(DetailView):
# 	template_name = 'reportes/detalle_ventas.html'
# 	model = DetalleVenta
# 	context_object_name = 'detalle'


def ReportVendetalle(request):
	id = request.GET['id']
	detalle = DetalleVenta.objects.filter(venta=id)
	data = serializers.serialize(
		'json', detalle, fields=('cantidad','subtotal','item','descuento','recargo','ice','excentos','scf'), use_natural_keys=True)
	return HttpResponse(data, content_type='application/json')

# def detalleVenta(request, pk):
#     print pk
#     venta = Venta.objects.filter(id=pk)
#     detalle = DetalleVenta.objects.filter(venta=venta)

#     vd = []
#     for d in detalle:
#         vd.append(d)

#     print vd

#     data = {
#         'nit': venta[0].nit,
#         'razon_social': venta[0].razon_social,
#         'fecha': venta[0].fecha,
#         'tipo_compra': venta[0].tipo_compra,
#         'total': venta[0].total,
#         'detalle': vd
        
#     }

#     print venta
#     return render(request, 'reportes/rep_detalleventa.html', data, context_instance=ctx(request))


def detalleVenta(request, pk):
    print pk
    venta = Venta.objects.filter(id=pk)
    detalle = DetalleVenta.objects.filter(venta=venta)
    
    vd = []
    for d in detalle:
        vd.append(d)

    print vd

    data = {
        'nit': venta[0].nit,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'total': venta[0].total,
        'detalle': vd
        
    }

    return render_to_pdf('reportes/rep_detalleventa.html', data)


def report_mesVenta(request):
    template_name = "reportes/rep_ventaMes.html"
    town = None

    if request.method == 'POST':
        date1 = request.POST['mes']
        anio = request.POST['anio']
        # obtencion del mes en texto
        d = date(int(anio),int(date1),1).strftime('%B')
        mes = _(d)
        # obtencion del año actual
        # today = date.today().year

        try:
        	# obteniendo datos del modelo venta 
	    	ventas = Venta.objects.filter(fecha__year=anio, fecha__month=date1)
	    	total = 0
	        for venta in ventas:
				total += venta.total

	        if 'excel' in request.POST:
	            response = HttpResponse(content_type='application/vnd.ms-excel')
	            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	            xlsx_data = WriteToExcel(ventas, mes, total, town)
	            response.write(xlsx_data)
	            return response

	        if 'pdf' in request.POST:
	            response = HttpResponse(content_type='application/pdf')
	            today = date.today()
	            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
	            response['Content-Disposition'] =\
	                'attachement; filename={0}.pdf'.format(filename)
	            buffer = BytesIO()
	            report = PdfPrint(buffer, 'A4')
	            pdf = report.report(ventas, 'REPORTE DE VENTAS', total, mes)
	            response.write(pdf)
	            return response

	        if 'txt' in request.POST:
	            response = HttpResponse(content_type='text/plain; charset=utf-8')
	            response['Content-Disposition'] = 'attachment; filename="output_three.txt"'
	            t = loader.get_template('reportes/output.txt')
	            c = Context({'ventas' : ventas, })

	            response.write(t.render(c))
	            return response

	    	context = {
		        'town': town,
		        'ventas': ventas,
		    }

	        return render(request, template_name, context)
        except Exception, e:
            messages.error(request, 'No existen ventas')

    return render(request, template_name)


def report_almacenes(request):
    template_name = "reportes/report_almacenes.html"
    town = None

    if request.method == 'POST':   

        # try:
        	# obteniendo datos del modelo venta 
	    	items = Item.objects.all()
	    	# datos = []
	     #    for it in items:
	        
	     #    	datos.append({
	     #    		'codigo_item': it.codigo_item,
	     #    		'codigo_fabrica': it.codigo_fabrica,
	     #    		'almacen': it.almacen,
	     #    		'grupo': it.grupo,
	     #    		'subgrupo': it.subgrupo,
	     #    		'descripcion': it.descripcion,
	     #    		'carac_especial_1': it.carac_especial_1,
	     #    		'carac_especial_2': it.carac_especial_2,
	     #    		'cantidad': it.cantidad,
	     #    		'saldo_min': it.saldo_min,
	     #    		'proveedor': it.proveedor.razon_social,
	     #    		'unidad_medida': it.unidad_medida,
	     #    		'costo_unitario': it.costo_unitario,
	     #    		'precio_unitario': it.precio_unitario,
	     #    		'total_costo': it.cantidad * it.costo_unitario,
	     #    		'total_precio': it.cantidad * it.precio_unitario
	     #    		})


	    	total = 0
	    	mes = 0
	   #      for venta in items:
				# total += venta.total

	        if 'excel' in request.POST:
	            response = HttpResponse(content_type='application/vnd.ms-excel')
	            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	            xlsx_data = WriteToAlmacen(items, mes, total, town)
	            response.write(xlsx_data)
	            return response

	        if 'pdf' in request.POST:
	            response = HttpResponse(content_type='application/pdf')
	            today = date.today()
	            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
	            response['Content-Disposition'] =\
	                'attachement; filename={0}.pdf'.format(filename)
	            buffer = BytesIO()
	            report = PdfAlmacen(buffer, 'A4')
	            pdf = report.report(items, 'REPORTE DE ALMACENES', total, mes)
	            response.write(pdf)
	            return response

	        if 'txt' in request.POST:
	            response = HttpResponse(content_type='text/plain; charset=utf-8')
	            response['Content-Disposition'] = 'attachment; filename="output_almacenes.txt"'
	            t = loader.get_template('reportes/almacenes.txt')

	            c = Context({'items' : items, })

	            response.write(t.render(c))
	            return response

	    	context = {
		        'town': town,
		        'ventas': ventas,
		    }

	        return render(request, template_name, context)
        # except Exception, e:
        #     messages.error(request, 'No existen ventas')

    return render(request, template_name)


def libro_compras(request):

    template_name = "reportes/libro_compras.html"
    town = None

    if request.method == 'POST':
        date1 = request.POST['mes']
        anio = request.POST['anio']
        # obtencion del mes en texto
        d = date(int(anio),int(date1),1).strftime('%B')
        mes = _(d)

        # try:
        	# obteniendo datos del modelo venta 
    	compras = Compra.objects.filter(fecha__year=anio, fecha__month=date1)
    	total = 0
        for compra in compras:
			total += compra.total

        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=Reporte_compras.xlsx'
            xlsx_data = WriteToCompras(compras, mes, total, town)
            response.write(xlsx_data)
            return response

        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfCompras(buffer, 'A4')
            pdf = report.report(compras, 'LIBRO DE COMPRAS', total, mes)
            response.write(pdf)
            return response

        if 'txt' in request.POST:
            response = HttpResponse(content_type='text/plain; charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="libro_compras.txt"'
            t = loader.get_template('reportes/lib_compras.txt')
            c = Context({'compras' : compras, })

            response.write(t.render(c))
            return response

    	context = {
	        'town': town,
	        'compras': compras,
	    }

        return render(request, template_name, context)
        # except Exception, e:
        #     messages.error(request, 'No existen ventas')

    return render(request, template_name)


def libro_ventas(request):

    template_name = "reportes/libro_ventas.html"
    town = None

    if request.method == 'POST':
        date1 = request.POST['mes']
        anio = request.POST['anio']
        # obtencion del mes en texto
        d = date(int(anio), int(date1), 1).strftime('%B')
        mes = _(d)

        # try:
        	# obteniendo datos del modelo venta 
    	ventas = Venta.objects.filter(fecha__year=anio, fecha__month=date1)
    	total = 0
        for venta in ventas:
			total += venta.total

        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=libro_ventas.xlsx'
            xlsx_data = WriteToVentas(ventas, mes, total, town)
            response.write(xlsx_data)
            return response

        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfVentas(buffer, 'A4')
            pdf = report.report(ventas, 'LIBRO DE VENTAS', total, mes)
            response.write(pdf)
            return response

        if 'txt' in request.POST:
            response = HttpResponse(content_type='text/plain; charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="libro_ventas.txt"'
            t = loader.get_template('reportes/lib_ventas.txt')
            c = Context({'ventas': ventas, })

            response.write(t.render(c))
            return response

    	context = {
	        'town': town,
	        'compras': ventas,
	    }

        return render(request, template_name, context)
        # except Exception, e:
        #     messages.error(request, 'No existen ventas')

    return render(request, template_name)


def ReportAlmacen(request):
	if request.method == 'POST':
		date1 = request.POST['date1']
		date2 = request.POST['date2']
		# tipo = request.POST['valuacion']

		if date1 != '':
			items = Item.objects.filter(fecha_transaccion__range=(date1, date2))
			total = 0

			for it in items:
				total += it.cantidad * it.precio_unitario
			
			return render(request, 'reportes/reporte_almacenes.html', {'items': items, 'total': total, 'ex': True, 'date1': date1, 'date2': date2})

	return render(request, 'reportes/reporte_almacenes.html')


def KardexAlmacen(request, pk):
    venta = Venta.objects.filter(id=pk)
    detalle = DetalleVenta.objects.filter(venta=venta)
    
    vd = []
    for d in detalle:
        vd.append(d)

    print vd

    data = {
        'nit': venta[0].nit,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'total': venta[0].total,
        'detalle': vd
        
    }

    return render_to_pdf('reportes/rep_detalleventa.html', data)
