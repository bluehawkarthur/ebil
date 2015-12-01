# -*- coding: utf-8 -*-
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
import xlsxwriter
import json
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponseBadRequest,HttpResponse


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
		'json', producto, fields=('codigo_item','descripcion',))
	else:
		descripcion = Item.objects.filter(descripcion__contains=idProducto)
		data = serializers.serialize(
		'json', descripcion, fields=('codigo_item','descripcion',))
	return HttpResponse(data, content_type='application/json')

def buscarEmpresa(request):

	idEmpresa = request.GET['id']
	producto = Venta.objects.filter(razon_social__contains=idEmpresa)
	if producto:
		data = serializers.serialize(
		'json', producto, fields=('razon_social','nit',))
	else:
		nit = Venta.objects.filter(nit__contains=idEmpresa)
		data = serializers.serialize(
		'json', nit, fields=('razon_social','nit',))

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

class Reporteventa(TemplateView):
	template_name = 'reportes/reporte_venta.html'

	def post(self, request, *args, **kwargs):
		date1 = request.POST['date1']
		date2 = request.POST['date2']
		tipo = request.POST['tipo_venta']
		nit = request.POST['nit2']
		monto = request.POST['monto2']


		if date1 != '':
			if nit != '':
				ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, nit=nit)
			elif monto != '':
				ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, total__gte=monto)
			else:
				ventas = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo)
			
			total = 0
			for venta in ventas:
				total += venta.total
			
			return render(request, 'reportes/reporte_venta.html', {'ventas':ventas, 'total':total, 'ex':True})
		else:
			return render(request, 'reportes/reporte_venta.html', {'ex':False})


# class ReportVendetalle(DetailView):
# 	template_name = 'reportes/detalle_ventas.html'
# 	model = DetalleVenta
# 	context_object_name = 'detalle'

def ReportVendetalle(request):
	id= request.GET['id']
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

def excel(request):
	# Create a workbook and add a worksheet.
	workbook = xlsxwriter.Workbook('Expenses01.xlsx')
	worksheet = workbook.add_worksheet('sheet1')

	# Some data we want to write to the worksheet.
	expenses = (
		['Rent', 1000],
		['Gas',   100],
		['Food',  300],
		['Gym',    50],
	)

	# Start from the first cell. Rows and columns are zero indexed.
	row = 0
	col = 0

	# Iterate over the data and write it out row by row.
	for item, cost in (expenses):
		worksheet.write(row, col,     item)
		worksheet.write(row, col + 1, cost)
		row += 1

	# Write a total using a formula.
	worksheet.write(row, 0, 'Total')
	worksheet.write(row, 1, '=SUM(B1:B4)')

	workbook.close()

	return HttpResponse(open('Expenses01.xlsx','r').read(), content_type='application/ms-excel')


# def generar_pdf(request):
# 	print "Genero el PDF"
# 	response = HttpResponse(content_type='application/pdf')
# 	pdf_name = "clientes.pdf"
# 	# llamado clientes
# 	# la linea 26 es por si deseas descargar el pdf a tu computadora
# 	# response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
# 	buff = BytesIO()
# 	doc = SimpleDocTemplate(buff,
# 							pagesize=letter,
# 							rightMargin=40,
# 							leftMargin=40,
# 							topMargin=60,
# 							bottomMargin=18,
# 							)
# 	clientes = []
# 	styles = getSampleStyleSheet()
# 	header = Paragraph("Listado de Clientes", styles['Heading1'])
# 	clientes.append(header)
# 	headings = ('Nombre', 'Email', 'Edad', 'Dirección', 'total')
# 	allclientes = [(p.nit, p.razon_social, p.tipo_compra, p.total) for p in Venta.objects.all()]
# 	# print allclientes

# 	t = Table([headings] + allclientes)
# 	print t
# 	t.setStyle(TableStyle(
# 		[
# 			('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
# 			('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
# 			('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
			
# 		]
# 	))
# 	clientes.append(t)
# 	doc.build(clientes)
# 	response.write(buff.getvalue())
# 	buff.close()
# 	return response