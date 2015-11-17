# views.py
from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import Venta, DetalleVenta
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest,HttpResponse
from django.core import serializers
import json
from apps.producto.models import Item
from django.db import transaction
from django.contrib import messages
from apps.producto.models import Item
import decimal



def buscarProducto(request):
    idProducto = request.GET['id']
    descripcion = Item.objects.filter(descripcion__contains=idProducto)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk','codigo_item','codigo_fabrica', 'descripcion', 'precio_unitario', 'unidad_medida'))
    else:
        producto = Item.objects.filter(codigo_item__contains=idProducto)
        data = serializers.serialize(
            'json', producto, fields=('pk','codigo_item','codigo_fabrica', 'descripcion', 'precio_unitario', 'unidad_medida'))
    return HttpResponse(data, content_type='application/json')


def ventaCrear(request):

    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print proceso

            total = 0
            # calculo total de compras
            for k in proceso['producto']:
                total += decimal.Decimal(k['sdf'])

            print total
            crearVenta = Venta(
                nit=proceso['nit'],
                razon_social=proceso['razon'],
                fecha=proceso['fecha'],
                tipo_compra=proceso['tipo_compra'],
                cantidad_dias=proceso['dias'],
                total=total,
            )
            crearVenta.save()

            for k in proceso['producto']:
             
                item = Item.objects.filter(id=k['pk'])
                cantidad_total = item[0].cantidad - int(k['cantidad'])
                print cantidad_total
                item.update(cantidad=cantidad_total)

                crearDetalle = DetalleVenta(
                    venta=crearVenta,
                    item=Item.objects.get(id=k['pk']),
                    cantidad=int(k['cantidad']),
                    subtotal=decimal.Decimal(k['subtotal']),
                    descuento=decimal.Decimal(k['descuentos']),
                    recargo=decimal.Decimal(k['recargos']),
                    ice=decimal.Decimal(k['ice']),
                    excentos=decimal.Decimal(k['excentos']),
                    scf=decimal.Decimal(k['sdf']),
                    tipo_descuento=k['tipo_descuento'],
                    tipo_recargo=k['tipo_recargo'],

                )

                crearDetalle.save()
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

    print venta
    return render('ventas/detalle.html', data, context_instance=ctx(request))