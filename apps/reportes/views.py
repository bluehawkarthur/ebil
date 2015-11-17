from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from apps.compras.models import Compra, DetalleCompra
from apps.ventas.models import Venta, DetalleVenta
from apps.producto.models import Item

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
		if date1 != '':
			ventas = Venta.objects.filter(fecha__range=(date1, date2))
			total = 0
			for venta in ventas:
				total += venta.total
			print total
			return render(request, 'reportes/reporte_venta.html', {'ventas':ventas, 'total':total, 'ex':True})
		else:
			return render(request, 'reportes/reporte_venta.html', {'ex':False})