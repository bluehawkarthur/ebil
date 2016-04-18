# views.py
# -*- coding: utf-8 -*-
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
from .numero_autorizacion import codigoControl
from apps.config.models import DatosDosificacion, Formatofactura, FacturaCampos, Sucursal

from django.http import HttpResponse
import json
from django.core import serializers

# personalize de configuracions de almacees y producto 
def configfactura(request):
    config = FacturaCampos.objects.filter(empresa=request.user.empresa)
    data = serializers.serialize(
          'json', config, fields=('descuento_usar', 'descuento_requerido', 'recargo_usar', 'recargo_requerido', 
    'ice_usar', 'ice_requerido', 'exentos_usar', 'exentos_requerido', 
    'tipos_venta_usar', 'tipos_venta_requerido'))
    return HttpResponse(data, content_type="application/json")
 


def buscarProducto(request):
    idProducto = request.GET['id']
    descripcion = Item.objects.filter(descripcion__icontains=idProducto, empresa=request.user.empresa)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk', 'codigo_item', 'codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    else:
        producto = Item.objects.filter(codigo_item__contains=idProducto, empresa=request.user.empresa)
        data = serializers.serialize(
            'json', producto, fields=('pk', 'codigo_item', 'codigo_fabrica', 'descripcion', 'cantidad', 'precio_unitario', 'unidad_medida'))
    return HttpResponse(data, content_type='application/json')


def buscarCliente(request):
    idCliente = request.GET['id']

    descripcion = Cliente.objects.filter(razonsocial__icontains=idCliente, empresa=request.user.empresa)
    

    if descripcion:
        data = serializers.serialize('json', descripcion, fields=('pk', 'nit', 'razonsocial'))
    else:
        nit = Cliente.objects.filter(nit__contains=idCliente, empresa=request.user.empresa)
        data = serializers.serialize('json', nit, fields=('pk', 'nit', 'razonsocial'))
    return HttpResponse(data, content_type='application/json')




def ventaCrear(request):


    form = None
    sucursal = Sucursal.objects.filter(empresa=request.user.empresa).order_by('pk')
    if request.method == 'POST':
        sid = transaction.savepoint()

        try:
            proceso = json.loads(request.POST.get('proceso'))

            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)
            print 'sucursalessssss'
            print proceso['sucursal']
            total = 0
            
            # calculo total de compras
            for k in proceso['producto']:
                total += decimal.Decimal(k['sdf'])

            if proceso['movimiento'] == 'facturar':
                venta_data = Venta.objects.filter(empresa=request.user.empresa, tipo_movimiento='facturar').exclude(nro_factura__isnull=True).last()
                print 'numerooo de facturaaaaaaa'
                print venta_data.nro_factura
                dosificacion = DatosDosificacion.objects.filter(empresa=request.user.empresa, sucursal=proceso['sucursal']).last()
                cliente = Cliente.objects.filter(nit=proceso['nit'])
                if not cliente:
                    cli = Cliente(
                        razonsocial=proceso['razon'],
                        nit=proceso['nit'],
                        empresa=request.user.empresa,
                    )
                    cli.save()
                print dosificacion
                if dosificacion !=  None:
                    print 'facturaaaaaaaaa'
                    if dosificacion.fecha >= datetime.date.today():
                        nro_init2 = int(dosificacion.nro_conrelativo)
                        contador = dosificacion.contador

                        nro_init = int(dosificacion.nro_conrelativo) - 1
                        if venta_data and (venta_data.nro_factura-contador)==nro_init2:
                            contador = contador + 1
                            dos = DatosDosificacion.objects.filter(id=dosificacion.pk)
                            dos.update(contador=contador)
                            nro = venta_data.nro_factura
                            if nro is None:
                                nro = nro_init
                        else:
                            nro = nro_init

                        fecha_venta = datetime.datetime.strptime(proceso['fecha'], "%Y-%m-%d").strftime("%Y-%m-%d")
                        cod_control = codigoControl(dosificacion.llave_digital, dosificacion.nro_autorizacion, nro + 1, proceso['nit'], fecha_venta, total, request.user.empresa.nit, total)

                        print 'el cogigo en venta', cod_control
                        
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
                            empresa=request.user.empresa,
                            numero_autorizacion=dosificacion.nro_autorizacion,
                            llave_digital=dosificacion.llave_digital,
                            codigo_control=cod_control,
                            fecha_limite=dosificacion.fecha,
                            tipo_movimiento=proceso['movimiento'],
                            sucursal=Sucursal.objects.get(id=proceso['sucursal']),
                            actividad=dosificacion.actividad,
                        )
                        
                        crearVenta.save()

                        for k in proceso['producto']:
                         
                            item = Item.objects.filter(id=k['pk'])
                            cantidad_total = item[0].cantidad - int(k['cantidad'])
                            
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

                            detalle = '%s a %s s/g factura Nro. %s' % ('Venta', proceso['razon'], nro + 1)

                            crearMovimiento = Movimiento(
                                cantidad=int(k['cantidad']),
                                precio_unitario=item[0].precio_unitario,
                                detalle=detalle,
                                fecha_transaccion=proceso['fecha'],
                                motivo_movimiento='salida',
                                item=Item.objects.get(id=k['pk']),
                                empresa=request.user.empresa,
                            )

                            crearDetalle.save()
                            crearMovimiento.save()

                        return render('ventas/venta.html', {'form': form, 'popup': True, 'pk': crearVenta.pk, 'sucursal': sucursal, 'url': '/detalle_venta/' }, context_instance=ctx(request))
                        # return HttpResponseRedirect(reverse('detalleventa', args=(crearVenta.pk,)))
                        # return HttpResponse('<script type="text/javascript">opener.popup("/detalle_venta/%s");</script>' % \
                        	# (crearVenta.pk))
                        # return HttpResponse('<script type="text/javascript">opener.popup("/detalle_venta/%s");opener.location.href = "/";</script>' % (crearVenta.pk))
                        # messages.success(
                        #     request, 'La compra se ha realizado satisfactoriamente')
                    else:
                        messages.error(request, 'La fecha limite de emision de la factura a caducado')
                else:
                        messages.error(request, 'Registre sus dosificaciones para que pueda realizar sus facturaciones')

            elif proceso['movimiento'] == 'baja':
                for k in proceso['producto']:
                    item = Item.objects.filter(id=k['pk'])
                    cantidad_total = item[0].cantidad - int(k['cantidad'])
                    print cantidad_total
                    item.update(cantidad=cantidad_total, fecha_transaccion=proceso['fecha'])
                    crearMovimiento = Movimiento(
                        cantidad=int(k['cantidad']),
                        precio_unitario=item[0].precio_unitario,
                        detalle='Baja',
                        fecha_transaccion=proceso['fecha'],
                        motivo_movimiento='salida',
                        item=Item.objects.get(id=k['pk']),
                        empresa=request.user.empresa,
                    )
                    crearMovimiento.save()
                return HttpResponseRedirect(reverse('registrarventas'))

            elif proceso['movimiento'] == 'proforma':

                venta_data = Venta.objects.filter(empresa=request.user.empresa).exclude(nro_nota__isnull=True).last()

                if venta_data:
                    nro = venta_data.nro_nota
                    if nro is None:
                        nro = 0
                else:
                    nro = 0

                cliente = Cliente.objects.filter(nit=proceso['nit'])
                if not cliente:
                    cli = Cliente(
                        razonsocial=proceso['razon'],
                        nit=proceso['nit'],
                        empresa=request.user.empresa,
                    )
                    cli.save()

                if proceso['tipo_compra'] == 'credito':
                    date_1 = datetime.datetime.strptime(proceso['fecha'], "%Y-%m-%d")
                    end_date = date_1 + datetime.timedelta(days=int(proceso['dias']))
                    today = datetime.date.today()

                else:
                    end_date = None

                crearVenta = Venta(
                    nit=proceso['nit'],
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
                    empresa=request.user.empresa,
                    tipo_movimiento=proceso['movimiento'],
                    nro_nota=nro+1,
                    sucursal=Sucursal.objects.get(id=proceso['sucursal']),
                )

                crearVenta.save()

                for k in proceso['producto']:

                    item = Item.objects.filter(id=k['pk'])
                    cantidad_total = item[0].cantidad - int(k['cantidad'])

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

                    detalle = '%s a %s s/g nota Nro. %s' % ('Venta', proceso['razon'],nro+1)

                    crearMovimiento = Movimiento(
                        cantidad=int(k['cantidad']),
                        precio_unitario=item[0].precio_unitario,
                        detalle=detalle,
                        fecha_transaccion=proceso['fecha'],
                        motivo_movimiento='salida',
                        item=Item.objects.get(id=k['pk']),
                        empresa=request.user.empresa,
                    )

                    crearDetalle.save()
                    crearMovimiento.save()

                # return HttpResponseRedirect(reverse('detalleventanota', args=(crearVenta.pk,)))
                return render('ventas/venta.html', {'form': form, 'popup': True, 'pk': crearVenta.pk, 'sucursal': sucursal, 'url': '/detalle_ventanota/'}, context_instance=ctx(request))

                # messages.success(
                #     request, 'La compra se ha realizado satisfactoriamente')

        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    return render('ventas/venta.html', {'form': form, 'sucursal': sucursal}, context_instance=ctx(request))

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
    venta = Venta.objects.filter(id=pk)
    detalle = DetalleVenta.objects.filter(venta=venta)

    vd = []
    scf = 0
    for d in detalle:
        scf = scf + d.scf
        vd.append(d)

    formato = Formatofactura.objects.get(empresa=request.user.empresa)
    # dosificacion = DatosDosificacion.objects.filter(empresa=request.user.empresa).last()
    # cod_control = codigoControl(dosificacion.llave_digital, dosificacion.nro_autorizacion, venta[0].nro_factura, venta[0].nit, venta[0].fecha, venta[0].total, request.user.empresa.nit,scf)
    
    data = {
        'nit': venta[0].nit,
        'nro_factura': venta[0].nro_factura,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'codigo_control': venta[0].codigo_control,
        'total': venta[0].total,
        'detalle': vd,
        'formato': formato,
        'numero_autorizacion': venta[0].numero_autorizacion,
        'fecha_limite': venta[0].fecha_limite,
        'empresa': request.user.get_empresa()

    }

    formato = Formatofactura.objects.get(empresa=request.user.empresa)
    print 'el formato'
    print formato

    if formato.impresion == 'Vacia':
        if formato.tamanio == 'rollo':
            return render_to_pdf('reportes/rep_detalleventarollo.html', data)

        elif formato.tamanio == 'carta':
            return render_to_pdf('reportes/rep_detalleventa.html', data)

        elif formato.tamanio == 'oficio':
            return render_to_pdf('reportes/rep_ventaoficio.html', data)

        elif formato.tamanio == '1/2oficio':
            return render_to_pdf('reportes/rep_ventamedio.html', data)

    elif formato.impresion == 'Completa':
        if formato.tamanio == 'rollo':
            return render_to_pdf('reportes/rep_detalleventarollo.html', data)

        elif formato.tamanio == 'carta':
            return render_to_pdf('reportes/rep_detalleventacompleta.html', data)

        elif formato.tamanio == 'oficio':
            return render_to_pdf('reportes/rep_ventaoficiocompleta.html', data)

        elif formato.tamanio == '1/2oficio':
            return render_to_pdf('reportes/rep_ventamediocompleta.html', data)

    elif formato.impresion == 'Semi-completa':
        if formato.tamanio == 'rollo':
            return render_to_pdf('reportes/rep_detalleventarollo.html', data)

        elif formato.tamanio == 'carta':
            return render_to_pdf('reportes/rep_detalleventasemi.html', data)

        elif formato.tamanio == 'oficio':
            return render_to_pdf('reportes/rep_ventaoficiosemi.html', data)

        elif formato.tamanio == '1/2oficio':
            return render_to_pdf('reportes/rep_ventamediosemi.html', data)


def detalleVentaNota(request, pk):
    venta = Venta.objects.filter(id=pk)
    detalle = DetalleVenta.objects.filter(venta=venta)

    vd = []
    scf = 0
    for d in detalle:
        scf = scf + d.scf
        vd.append(d)

    formato = Formatofactura.objects.get(empresa=request.user.empresa)
    # dosificacion = DatosDosificacion.objects.filter(empresa=request.user.empresa).last()
    # cod_control = codigoControl(dosificacion.llave_digital, dosificacion.nro_autorizacion, venta[0].nro_factura, venta[0].nit, venta[0].fecha, venta[0].total, request.user.empresa.nit,scf)
    
    data = {
        'nit': venta[0].nit,
        'nro_nota': venta[0].nro_nota,
        'razon_social': venta[0].razon_social,
        'fecha': venta[0].fecha,
        'tipo_compra': venta[0].tipo_compra,
        'codigo_control': venta[0].codigo_control,
        'total': venta[0].total,
        'detalle': vd,
        'formato': formato,
        'numero_autorizacion': venta[0].numero_autorizacion,
        'fecha_limite': venta[0].fecha_limite,
        'empresa': request.user.get_empresa()

    }

    return render_to_pdf('reportes/rep_detalleventanota.html', data)

# def detalleVentarollo(request, pk):
#     print pk
#     venta = Venta.objects.filter(id=pk)
#     detalle = DetalleVenta.objects.filter(venta=venta)
    
#     vd = []
#     scf = 0
#     for d in detalle:
#         scf = scf + d.scf
#         vd.append(d)

#     dosificacion = DatosDosificacion.objects.filter(empresa=request.user.empresa).last()
#     # cod_control = codigoControl(dosificacion.llave_digital, dosificacion.nro_autorizacion, venta[0].nro_factura, venta[0].nit, venta[0].fecha, venta[0].total, request.user.empresa.nit,scf)
#     date_1 = datetime.datetime.strptime(str(dosificacion.fecha), "%Y-%m-%d").strftime("%d/%m/%Y")

#     data = {
#         'nit': venta[0].nit,
#         'nro_factura': venta[0].nro_factura,
#         'razon_social': venta[0].razon_social,
#         'fecha': venta[0].fecha,
#         'tipo_compra': venta[0].tipo_compra,
#         'codigo_control': venta[0].codigo_control,
#         'total': venta[0].total,
#         'detalle': vd,
#         'fecha_limite': date_1,

#     }

#     return render_to_pdf('reportes/rep_detalleventarollo.html', data)


def migrate(request):
    
    ventas = Venta.objects.all()
    # detalle = DetalleVenta.objects.filter(venta=ventas)
    for v in ventas:
        detalle = DetalleVenta.objects.filter(venta=v)
        if detalle:
            print 'tiene detalle', v.nit
        else:
            print 'noooo tiene', v.nit
    # for d in detalle:
    #     if d:
    #         print 'tiene detalle'
    #     else:
    #         print 'noooo tiene'
    # print r
    # date1 = '2015-11-1'
    # date2 = '2015-11-30'
    # ventas = Venta.objects.filter(fecha__range=(date1, date2))
    # detalle = DetalleVenta.objects.filter(venta=ventas)
    # print 'migrando datos xfavor spere ..........'
    # for v in detalle:
    #     print v.item.precio_unitario
    #     v.precio_unitario = v.item.precio_unitario
    #     v.save()
    #     detalle = '%s a %s' % ('Venta', v.venta.razon_social)

    #     crearMovimiento = Movimiento(
    #         cantidad=v.cantidad,
    #         precio_unitario=v.item.precio_unitario,
    #         detalle=detalle,
    #         fecha_transaccion=v.venta.fecha,
    #         motivo_movimiento='salida',
    #         item=Item.objects.get(id=v.item.pk),
    #     )

    #     crearMovimiento.save()


# def migrate(request):
#     ventas = Venta.objects.filter(tipo_compra='credito')
#     for v in ventas:
#         print v
#         date_1 = v.fecha
#         end_date = date_1 + datetime.timedelta(days=int(v.cantidad_dias))
#         v.fecha_vencimiento = end_date
#         v.save()