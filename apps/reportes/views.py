# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from apps.compras.models import Compra, DetalleCompra, CobroCompra
from apps.ventas.models import Venta, DetalleVenta, Movimiento, Cobro
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
import decimal
from .htmltopdf import render_to_pdf
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q
from apps.config.models import DatosDosificacion
from apps.ventas.numero_autorizacion import codigoControl


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
		# monto = request.POST['monto2']
		empresa = request.POST['empresa2']

		if date1 != '' and date2 != '':
			if tipo == 'todo':
				if nit != '':
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2), nit=nit)
					ventas = DetalleVenta.objects.filter(venta=ventas1)
				elif empresa != '':
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2), razon_social=empresa)
					ventas = DetalleVenta.objects.filter(venta=ventas1)
				# elif monto != '':
				# 	ventas1 = Venta.objects.filter(fecha__range=(date1, date2), total__gte=monto)
				# 	ventas = DetalleVenta.objects.filter(venta=ventas1)
				else:
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2))
					ventas = DetalleVenta.objects.filter(venta=ventas1)

			else:
				if nit != '':
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2), tipo_compra=tipo, nit=nit)
					ventas = DetalleVenta.objects.filter(venta=ventas1)
				elif empresa != '':
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2), tipo_compra=tipo, razon_social=empresa)
					ventas = DetalleVenta.objects.filter(venta=ventas1)
				# elif monto != '':
				# 	ventas1 = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, total__gte=monto)
				# 	ventas = DetalleVenta.objects.filter(venta=ventas1)
				else:
					ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha__range=(date1, date2), tipo_compra=tipo)
					ventas = DetalleVenta.objects.filter(venta=ventas1)
			
			total = 0
			for venta in ventas1:
				total += venta.total
			
			return render(request, 'reportes/reporte_venta.html', {'ventas': ventas, 'total': total, 'ex':True, 'date1': date1, 'date2': date2})
		else:
			return render(request, 'reportes/reporte_venta.html', {'valid': True, 'ex':True, 'date1': date1, 'date2': date2})
		
	else:
		datecompu = date.today()
		total = 0
		ventas1 = Venta.objects.filter(empresa=request.user.empresa, fecha=datecompu)
		ventas = DetalleVenta.objects.filter(venta=ventas1)
		for venta in ventas:
			total += venta.cantidad * venta.precio_unitario

		return render(request, 'reportes/reporte_venta.html', {'ventas': ventas, 'total': total, 'ex': True})
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
    scf = 0
    for d in detalle:
        scf = scf + d.scf
        vd.append(d)

    # dosificacion = DatosDosificacion.objects.filter(empresa=request.user.empresa).last()
    # cod_control = codigoControl(dosificacion.llave_digital, dosificacion.nro_autorizacion, venta[0].nro_factura, venta[0].nit, venta[0].fecha, venta[0].total, request.user.empresa.nit,scf)
    cod_control = codigoControl(venta[0].llave_digital, venta[0].numero_autorizacion, venta[0].nro_factura, venta[0].nit, venta[0].fecha, venta[0].total, request.user.empresa.nit,scf)
    print 'sssssssssssssss',cod_control
    data = {
        'nit': venta[0].nit,
        'nro_factura': venta[0].nro_factura,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'codigo_control': venta[0].codigo_control,
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
	    	ventas = Venta.objects.filter(empresa=request.user.empresa, fecha__year=anio, fecha__month=date1)
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
	    	items = Item.objects.filter(empresa=request.user.empresa)
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

        try:
        	
	    	compras = Compra.objects.filter(empresa=request.user.empresa, fecha__year=anio, fecha__month=date1)
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
        except Exception, e:
            messages.error(request, 'No existen compras')

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

        try:
        	# obteniendo datos del modelo venta
	    	ventas = Venta.objects.filter(empresa=request.user.empresa, fecha__year=anio, fecha__month=date1)
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
        except Exception, e:
            messages.error(request, 'No existen ventas')

    return render(request, template_name)


def ReportAlmacen(request):
    if request.method == 'POST':
        date1 = request.POST['mes']
        anio = request.POST['anio']

        items = Item.objects.filter(empresa=request.user.empresa, fecha_transaccion__year=anio, fecha_transaccion__month=date1)
        total = 0

        for it in items:
            total += it.cantidad * it.precio_unitario
        return render(request, 'reportes/reporte_almacenes.html', {'items': items, 'total': total, 'ex': True, 'date1': date1, 'anio': anio})
    return render(request, 'reportes/reporte_almacenes.html')


def KardexAlmacen(request, pk):
    venta = Venta.objects.filter(empresa=request.user.empresa, id=pk)
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


def promedios(request, pk, date1, anio):
    movimiento = Movimiento.objects.filter(empresa=request.user.empresa, item=pk, fecha_transaccion__year=anio, fecha_transaccion__month=date1).exclude(motivo_movimiento='inicial').order_by('fecha_transaccion')
    producto = Item.objects.get(id=pk)
    movimientoinit = Movimiento.objects.filter(empresa=request.user.empresa, item=pk, motivo_movimiento='inicial')
    datosfinal = []
    datosfinal.extend(movimientoinit)
    datosfinal.extend(movimiento)
    
    for d in datosfinal:
    	print d
    data = []
    saldo = 0
    saldov = 0

    for m in datosfinal:
        item = Item.objects.filter(id=pk)
        if m.motivo_movimiento == 'salida':
            saldo = saldo - m.cantidad
            salidav = m.precio_unitario * m.cantidad
            saldov = saldov - salidav

            data.append({
                'fecha': m.fecha_transaccion,
                'detalle': m.detalle,
                'pu': m.precio_unitario,
                'ingreso': 0,
                'salida': m.cantidad,
                'saldo': abs(saldo),
                'ingresov': 0,
                'salidav': salidav,
                'saldov': abs(saldov),
            })

        else:
            saldo = saldo + m.cantidad
            ingresov = m.precio_unitario * m.cantidad
            saldov = saldov + ingresov
            data.append({
                'fecha': m.fecha_transaccion,
                'detalle': m.detalle,
                'pu': m.precio_unitario,
                'ingreso': m.cantidad,
                'salida': 0,
                'saldo': saldo,
                'ingresov': ingresov,
                'salidav': 0,
                'saldov': saldov,
            })

    return render(request, 'reportes/reporte_kardex.html', {'kardex': data, 'item': producto})


def Createpago(request):

    if request.method == 'POST':
        monto = request.POST['monto']
        venta = request.POST['venta']
        venta_get = Venta.objects.filter(empresa=request.user.empresa, id=venta)
        crearcobro = Cobro(
            venta=Venta.objects.get(id=venta),
            monto_pago=monto,
            fecha_transaccion=date.today(),
            empresa=request.user.empresa,
        )
        crearcobro.save()

        if venta_get[0].monto_pago is None:
            montofinal = venta_get[0].total - decimal.Decimal(monto)
            if montofinal == 0:
                venta_get.update(tipo_compra='contado', monto_pago=monto)
            else:
                venta_get.update(monto_pago=monto)
        else:
            monto2 = venta_get[0].monto_pago + decimal.Decimal(monto)
            montofinal = venta_get[0].total - monto2
            if montofinal == 0:
                venta_get.update(tipo_compra='contado', monto_pago=monto2)
            else:
                venta_get.update(monto_pago=monto2)

        # montofinal = venta_get[0].total - decimal.Decimal(monto)
        # venta_get.update(monto_pago=montofinal)
        print monto
        data = {
            'monto': monto,
            'cliente': venta_get[0].razon_social,
            'fecha': date.today(),
        }

    return render_to_pdf('reportes/reporte_pago.html', data)


class ReporteCaja(TemplateView):
	template_name = 'reportes/caja.html'
	success_url = reverse_lazy('rep_caja')

	def post(self, request, *args, **kwargs):
		hoy = request.POST['hoy']
		cajai = request.POST['si']
		gastos = request.POST['gd']
		

		if hoy != '':
#			ventas = Venta.objects.filter(fecha=hoy)
			ventas = Venta.objects.filter(Q(empresa=self.request.user.empresa) & Q(fecha=hoy) & Q(tipo_compra='contado'))
			cobros = Cobro.objects.filter(empresa=self.request.user.empresa, fecha_transaccion=date.today())
			totcobros = 0
			for x in cobros:
				totcobros = totcobros+x.monto_pago
			sub = 0
			for i in ventas:
				sub = sub+i.total
			total = decimal.Decimal(cajai)+sub-decimal.Decimal(gastos)+totcobros
			print total


			return render_to_pdf('reportes/ccaja.html', {'sub': sub, 'cajai': cajai, 'gastos': gastos, 'total': total, 'ventas': ventas, 'cobros': cobros, 'totcobros': totcobros})
		else:
			ventas = Venta.objects.filter(empresa=self.request.user.empresa, fecha=hoy)
			return render(request, 'reportes/ccaja.html', {'ventas': ventas, 'cajai': cajai, 'gastos': gastos,'total': total, 'ventas': ventas, 'cobros': cobros, 'totcobros': totcobros})


def Reportcompra(request):
	if request.method == 'POST':
		date1 = request.POST['date1']
		date2 = request.POST['date2']
		tipo = request.POST['tipo_compra']
		nit = request.POST['nit2']
		# monto = request.POST['monto2']
		empresa = request.POST['empresa2']

		if date1 != '' and date2 != '':
			if tipo == 'todo':
				if nit != '':
					compra1 = Compra.objects.filter(fecha__range=(date1, date2), nit=nit)
					compras = DetalleCompra.objects.filter(compra=compra1)
				elif empresa != '':
					compra1 = Compra.objects.filter(fecha__range=(date1, date2), razon_social=empresa)
					compras = DetalleCompra.objects.filter(compra=compra1)
				# elif monto != '':
				# 	compra1 = Venta.objects.filter(fecha__range=(date1, date2), total__gte=monto)
				# 	compras = DetalleCompra.objects.filter(venta=compra1)
				else:
					compra1 = Compra.objects.filter(fecha__range=(date1, date2))
					compras = DetalleCompra.objects.filter(compra=compra1)

			else:
				if nit != '':
					compra1 = Compra.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, nit=nit)
					compras = DetalleCompra.objects.filter(compra=compra1)
				elif empresa != '':
					compra1 = Compra.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, razon_social=empresa)
					compras = DetalleCompra.objects.filter(compra=compra1)
				# elif monto != '':
				# 	compra1 = Venta.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo, total__gte=monto)
				# 	compras = DetalleCompra.objects.filter(venta=compra1)
				else:
					compra1 = Compra.objects.filter(fecha__range=(date1, date2), tipo_compra=tipo)
					compras = DetalleCompra.objects.filter(compra=compra1)
			
			total = 0
			for compra in compra1:
				total += compra.total
			
			return render(request, 'reportes/reporte_compra.html', {'compras': compras, 'total': total, 'ex':True, 'date1': date1, 'date2': date2})
		else:
			return render(request, 'reportes/reporte_compra.html', {'valid': True, 'ex':True, 'date1': date1, 'date2': date2})
		
	else:
		datecompu = date.today()
		total = 0
		compra1 = Compra.objects.filter(fecha=datecompu)
		compras = DetalleCompra.objects.filter(compra=compra1)
		for compra in compras:
			total += compra.cantidad * compra.precio_unitario

		return render(request, 'reportes/reporte_compra.html', {'compras': compras, 'total': total, 'ex': True})


def detalleCompra(request, pk):
    compra = Compra.objects.filter(id=pk)
    detalle = DetalleCompra.objects.filter(compra=compra)
    vd = []
    for d in detalle:
        vd.append(d)


    data = {
        'nit': compra[0].nit,
        'nro_factura': compra[0].nro_factura,
        'razon_social': compra[0].razon_social,
        'fecha': compra[0].fecha,
        'tipo_compra': compra[0].tipo_compra,
        'total': compra[0].total,
        'detalle': vd
        
    }

    return render_to_pdf('reportes/rep_detallecompra.html', data)


def Createpagocobro(request):

    if request.method == 'POST':
        monto = request.POST['monto']
        compra = request.POST['compra']
        compra_get = Compra.objects.filter(id=compra)

        crearcobro = CobroCompra(
            compra=Compra.objects.get(id=compra),
            monto_pago=monto,
            fecha_transaccion=date.today(),
        )
        crearcobro.save()

        if compra_get[0].monto_pago is None:
            montofinal = compra_get[0].total - decimal.Decimal(monto)
            if montofinal == 0:
                compra_get.update(tipo_compra='contado', monto_pago=monto)
            else:
                compra_get.update(monto_pago=monto)
        else:
            monto2 = compra_get[0].monto_pago + decimal.Decimal(monto)
            montofinal = compra_get[0].total - monto2
            if montofinal == 0:
                compra_get.update(tipo_compra='contado', monto_pago=monto2)
            else:
                compra_get.update(monto_pago=monto2)

        # montofinal = venta_get[0].total - decimal.Decimal(monto)
        # venta_get.update(monto_pago=montofinal)
        print monto
        data = {
            'monto': monto,
            'cliente': compra_get[0].razon_social,
            'fecha': date.today(),
        }

    return render_to_pdf('reportes/reporte_pagocompra.html', data)