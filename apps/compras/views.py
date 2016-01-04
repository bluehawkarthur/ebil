# views.py
from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import Compra, DetalleCompra
from .forms import CompraForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core import serializers
import json
from apps.producto.models import Item
from django.db import transaction
from django.contrib import messages
from apps.producto.models import Item
from apps.ventas.models import Movimiento
import decimal
from apps.reportes.htmltopdf import render_to_pdf
from datetime import date


class Success(TemplateView):
	template_name='compras/success.html'


def buscarProducto(request):
    idProducto = request.GET['id']
    descripcion = Item.objects.filter(descripcion__contains=idProducto)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk','codigo_item','codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    else:
        producto = Item.objects.filter(codigo_item__contains=idProducto)
        data = serializers.serialize(
            'json', producto, fields=('pk','codigo_item','codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    return HttpResponse(data, content_type='application/json')


def compraCrear(request):

    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)
            # if proceso['nit'] == '':
            #     msg = 'Ingrese nit'
            #     raise Exception(msg)

            total = 0
            # calculo total de compras
            for k in proceso['producto']:
                total += decimal.Decimal(k['sdf'])

            print total
            crearCompra = Compra(
                nit=proceso['nit'],
                razon_social=proceso['razon'],
                nro_factura=proceso['nro_factura'],
                nro_autorizacion=proceso['nro_autorizacion'],
                fecha=proceso['fecha'],
                cod_control=proceso['codigo_control'],
                tipo_compra=proceso['tipo_compra'],
                cantidad_dias=proceso['dias'],
                total=total,
                descuento=proceso['descuento'],
                recargo=proceso['recargo'],
                ice=proceso['ice'],
                excentos=proceso['excentos'],
                tipo_descuento=proceso['tipo_descuento'],
                tipo_recargo=proceso['tipo_recargo'],

            )
            crearCompra.save()

            for k in proceso['producto']:
                if k['centro_costos'] == 'A':
                    item = Item.objects.filter(id=k['pk'])
                    cantidad_total = item[0].cantidad + int(k['cantidad'])
                    today = date.today()
                    item.update(cantidad=cantidad_total, precio_unitario=decimal.Decimal(k['precio_unitario']), fecha_transaccion=today)

                    crearDetalle = DetalleCompra(
                        compra=crearCompra,
                        producto=Item.objects.get(id=k['pk']),
                        codigo=k['codigo_item'],
                        cantidad=int(k['cantidad']),
                        unidad=k['unidad'],
                        detalle=k['detalle'],
                        precio_unitario=decimal.Decimal(k['precio_unitario']),
                        subtotal=decimal.Decimal(k['subtotal']),
                        descuento=decimal.Decimal(k['descuentos']),
                        recargo=decimal.Decimal(k['recargos']),
                        ice=decimal.Decimal(k['ice']),
                        excentos=decimal.Decimal(k['excentos']),
                        scf=decimal.Decimal(k['sdf']),
                        centro_costos=k['centro_costos'],
                        tipo_descuento=k['tipo_descuento'],
                        tipo_recargo=k['tipo_recargo'],

                    )

                    detalle = '%s a %s' % ('Compra', proceso['razon'])

                    crearMovimiento = Movimiento(
                        cantidad=int(k['cantidad']),
                        precio_unitario=decimal.Decimal(k['precio_unitario']),
                        detalle=detalle,
                        fecha_transaccion=proceso['fecha'],
                        motivo_movimiento='ingreso',
                        item=Item.objects.get(id=k['pk']),
                    )


                    crearDetalle.save()
                    crearMovimiento.save()

                else:
                    crearDetalle = DetalleCompra(
                        compra=crearCompra,
                        codigo=k['codigo_item'],
                        cantidad=int(k['cantidad']),
                        unidad=k['unidad'],
                        detalle=k['detalle'],
                        precio_unitario=decimal.Decimal(k['precio_unitario']),
                        subtotal=decimal.Decimal(k['subtotal']),
                        descuento=decimal.Decimal(k['descuentos']),
                        recargo=decimal.Decimal(k['recargos']),
                        ice=decimal.Decimal(k['ice']),
                        excentos=decimal.Decimal(k['excentos']),
                        scf=decimal.Decimal(k['sdf']),
                        centro_costos=k['centro_costos'],
                        tipo_descuento=k['tipo_descuento'],
                        tipo_recargo=k['tipo_recargo'],

                    )

                    crearDetalle.save()
            
            return HttpResponseRedirect(reverse('detallecompra', args=(crearCompra.pk,)))

           

        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    return render('compras/compra.html', {'form': form}, context_instance=ctx(request))


# def detalleCompra(request, pk):
#     print pk
#     compra = Compra.objects.filter(id=pk)
#     detalle = DetalleCompra.objects.filter(compra=compra)
    

#     vd = []
#     for d in detalle:
#         vd.append(d)

#     print vd

#     data = {
#         'nit': compra[0].nit,
#         'razon_social': compra[0].razon_social,
#         'nro_factura': compra[0].nro_factura,
#         'nro_autorizacion': compra[0].nro_autorizacion,
#         'fecha': compra[0].fecha,
#         'cod_control': compra[0].cod_control,
#         'tipo_compra': compra[0].tipo_compra,
#         'cantidad_dias': compra[0].cantidad_dias,
#         'total': compra[0].total,
#         'detalle': vd
        
#     }

#     print compra
#     return render('compras/detalle.html', data, context_instance=ctx(request))


def detalleCompra(request, pk):
    print pk
    compra = Compra.objects.filter(id=pk)
    detalle = DetalleCompra.objects.filter(compra=compra)
    

    vd = []
    for d in detalle:
        vd.append(d)

    print vd

    data = {
        'nit': compra[0].nit,
        'razon_social': compra[0].razon_social,
        'nro_factura': compra[0].nro_factura,
        'nro_autorizacion': compra[0].nro_autorizacion,
        'fecha': compra[0].fecha,
        'cod_control': compra[0].cod_control,
        'tipo_compra': compra[0].tipo_compra,
        'cantidad_dias': compra[0].cantidad_dias,
        'total': compra[0].total,
        'detalle': vd
        
    }
    messages.success(request, 'La compra se ha realizado satisfactoriamente')
    print compra
    return render_to_pdf('reportes/rep_detallecompra.html', data)
