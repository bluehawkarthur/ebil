# views.py
from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import Venta, DetalleVenta, Movimiento
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest,HttpResponse
from django.core import serializers
import json
from django.db import transaction
from django.contrib import messages
from apps.producto.models import Item
from apps.cliente.models import Cliente
import decimal
from apps.reportes.htmltopdf import render_to_pdf
import datetime


def buscarProducto(request):
    idProducto = request.GET['id']
    descripcion = Item.objects.filter(descripcion__contains=idProducto)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk', 'codigo_item', 'codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    else:
        producto = Item.objects.filter(codigo_item__contains=idProducto)
        data = serializers.serialize(
            'json', producto, fields=('pk', 'codigo_item', 'codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    return HttpResponse(data, content_type='application/json')


def buscarCliente(request):
    idCliente = request.GET['id']
    descripcion = Cliente.objects.filter(razonsocial__contains=idCliente)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk', 'nit', 'razonsocial'))
    else:
        nit = Cliente.objects.filter(nit__contains=idCliente)
        data = serializers.serialize(
            'json', nit, fields=('pk', 'nit', 'razonsocial'))
    return HttpResponse(data, content_type='application/json')


def ventaCrear(request):

    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)

            total = 0
            # calculo total de compras
            for k in proceso['producto']:
                total += decimal.Decimal(k['sdf'])

            venta_data = Venta.objects.all().last()

            if venta_data:
                nro = venta_data.nro_factura
                if nro is None:
                    nro = 0
            else:
                nro = 0

            if proceso['tipo_compra'] == 'credito':
                date_1 = datetime.datetime.strptime(proceso['fecha'], "%Y-%m-%d")
                end_date = date_1 + datetime.timedelta(days=int(proceso['dias']))
                today = datetime.date.today()
                
                print 'tiempo de fecha vencimiento'
                print (today-datetime.date(2016, 1, 12)).days
            else:
                end_date = None

            crearVenta = Venta(
                nit=proceso['nit'],
                nro_factura=nro + 1,
                razon_social=proceso['razon'],
                fecha=proceso['fecha'],
                tipo_compra=proceso['tipo_compra'],
                cantidad_dias=proceso['dias'],
                total=total,
                descuento=proceso['descuento'],
                recargo=proceso['recargo'],
                ice=proceso['ice'],
                excentos=proceso['excentos'],
                tipo_descuento=proceso['tipo_descuento'],
                tipo_recargo=proceso['tipo_recargo'],
                fecha_vencimiento=end_date,
            )
            crearVenta.save()

            for k in proceso['producto']:
             
                item = Item.objects.filter(id=k['pk'])
                cantidad_total = item[0].cantidad - int(k['cantidad'])
                print cantidad_total
                item.update(cantidad=cantidad_total, fecha_transaccion=proceso['fecha'])

                crearDetalle = DetalleVenta(
                    venta=crearVenta,
                    item=Item.objects.get(id=k['pk']),
                    cantidad=int(k['cantidad']),
                    precio_unitario=item[0].precio_unitario,
                    subtotal=decimal.Decimal(k['subtotal']),
                    descuento=decimal.Decimal(k['descuentos']),
                    recargo=decimal.Decimal(k['recargos']),
                    ice=decimal.Decimal(k['ice']),
                    excentos=decimal.Decimal(k['excentos']),
                    scf=decimal.Decimal(k['sdf']),
                    tipo_descuento=k['tipo_descuento'],
                    tipo_recargo=k['tipo_recargo'],

                )

                detalle = '%s a %s' % ('Venta', proceso['razon'])

                crearMovimiento = Movimiento(
                    cantidad=int(k['cantidad']),
                    precio_unitario=item[0].precio_unitario,
                    detalle=detalle,
                    fecha_transaccion=proceso['fecha'],
                    motivo_movimiento='salida',
                    item=Item.objects.get(id=k['pk']),
                )

                crearDetalle.save()
                crearMovimiento.save()

            if 'rollo' in request.POST:
                return HttpResponseRedirect(reverse('detalleventarollo', args=(crearVenta.pk,)))
            else:
                return HttpResponseRedirect(reverse('detalleventa', args=(crearVenta.pk,)))

            # messages.success(
            #     request, 'La compra se ha realizado satisfactoriamente')

        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    return render('ventas/venta.html', {'form': form}, context_instance=ctx(request))

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
#     return render('ventas/detalle.html', data, context_instance=ctx(request))

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
        'nro_factura': venta[0].nro_factura,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'total': venta[0].total,
        'detalle': vd
        
    }

    return render_to_pdf('reportes/rep_detalleventa.html', data)


def detalleVentarollo(request, pk):
    print pk
    venta = Venta.objects.filter(id=pk)
    detalle = DetalleVenta.objects.filter(venta=venta)
    
    vd = []
    for d in detalle:
        vd.append(d)

    print vd

    data = {
        'nit': venta[0].nit,
        'nro_factura': venta[0].nro_factura,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'total': venta[0].total,
        'detalle': vd
        
    }

    return render_to_pdf('reportes/rep_detalleventarollo.html', data)


def migrate(request):
    date1 = '2015-11-1'
    date2 = '2015-11-30'
    ventas = Venta.objects.filter(fecha__range=(date1, date2))
    detalle = DetalleVenta.objects.filter(venta=ventas)
    print 'migrando datos xfavor spere ..........'
    for v in detalle:
        print v.item.precio_unitario
        v.precio_unitario = v.item.precio_unitario
        v.save()
        detalle = '%s a %s' % ('Venta', v.venta.razon_social)

        crearMovimiento = Movimiento(
            cantidad=v.cantidad,
            precio_unitario=v.item.precio_unitario,
            detalle=detalle,
            fecha_transaccion=v.venta.fecha,
            motivo_movimiento='salida',
            item=Item.objects.get(id=v.item.pk),
        )

        crearMovimiento.save()


# def migrate(request):
#     ventas = Venta.objects.filter(tipo_compra='credito')
#     for v in ventas:
#         print v
#         date_1 = v.fecha
#         end_date = date_1 + datetime.timedelta(days=int(v.cantidad_dias))
#         v.fecha_vencimiento = end_date
#         v.save()