# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import ItemForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Item
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django import forms
from apps.proveedores.models import Proveedor
from apps.ventas.models import Movimiento

from django.shortcuts import render_to_response
from django.template import RequestContext
import django_excel as excel
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel as pe
import sys
PY2 = sys.version_info[0] == 2
if PY2:
    import pyexcel.ext.ods
else:
    import pyexcel.ext.ods3

from ebil.settings import MEDIA_ROOT

import os
import xlrd
from datetime import date

IMPORT_FILE_TYPES = ['.xls', '.xlsx', ]
from django.contrib import messages
import decimal
from django.db import IntegrityError

import xlsxwriter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.config.models import AlmacenesCampos
from django.http import HttpResponse
import json
from django.core import serializers

# personalize de configuracions de almacees y producto 
def configalmacen(request):
    config = AlmacenesCampos.objects.filter(empresa=request.user.empresa)
    data = serializers.serialize(
          'json', config, fields=('codigo_fabr_usar', 'codigo_fabr_reque', 'codigo_fabricatipo', 'codigo_fabricacaractr', 
    'caract_espec_usar', 'caract_espec_requerid', 'caract_espectipo', 'caract_especaractr', 
    'unidad_medid_usar', 'unidad_medid_requerido', 'unidad_medidatipo', 'unidad_medidacaractr', 'imagen_usar', 'imagen_requer', 'grupo_usar','grupo_requerido',
    'grupo_tipo', 'grupo_caractr', 'subgrupo_usar', 'subgrupo_requerido', 'subgrupo_tipo', 'subgrupo_caractr', 'carac_especial_2_usar',
    'carac_especial_2_requerido', 'carac_especial_2_tipo', 'carac_especial_2_caractr'))
    return HttpResponse(data, content_type="application/json")


class CrearItem(FormView):
    template_name = 'producto/crear_item.html'
    form_class = ItemForm
    success_url = reverse_lazy('listar_item')

    # personalize choices for user authenticate
    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.fields['proveedor'].queryset = Proveedor.objects.filter(
            empresa=self.request.user.empresa).all()
        return form

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrearItem, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        item = Item()
        item.codigo_item = form.cleaned_data['codigo_item']
        item.codigo_fabrica = form.cleaned_data['codigo_fabrica']
        item.almacen = form.cleaned_data['almacen']
        item.grupo = form.cleaned_data['grupo']
        item.subgrupo = form.cleaned_data['subgrupo']
        item.descripcion = form.cleaned_data['descripcion']
        item.carac_especial_1 = form.cleaned_data['carac_especial_1']
        item.carac_especial_2 = form.cleaned_data['carac_especial_2']
        item.cantidad = form.cleaned_data['cantidad']
        item.saldo_min = form.cleaned_data['saldo_min']
        item.proveedor = form.cleaned_data['proveedor']
        item.imagen = form.cleaned_data['imagen']
        item.unidad_medida = form.cleaned_data['unidad_medida']
        item.costo_unitario = form.cleaned_data['costo_unitario']
        item.precio_unitario = form.cleaned_data['precio_unitario']
        item.empresa = self.request.user.empresa
        today = date.today()
        movimiento = Movimiento()
        movimiento.cantidad = form.cleaned_data['cantidad']
        movimiento.precio_unitario = form.cleaned_data['precio_unitario']
        movimiento.detalle = 'Saldo Inicial'
        movimiento.fecha_transaccion = today.strftime('%Y-%m-%d')
        movimiento.motivo_movimiento = 'inicial'
        movimiento.empresa = self.request.user.empresa
        try:
            item.save()
        except IntegrityError:
            messages.error(self.request, "error CODIGO ITEM DUPLICADO")
            return self.form_invalid(form)
        movimiento.item = item
        movimiento.save()
        return super(CrearItem, self).form_valid(form)



from rolepermissions.mixins import HasRoleMixin


import operator
from django.db.models import Q
import itertools


class ListarItem(PaginationMixin, ListView):
    template_name = 'producto/listar_item.html'
    model = Item
    paginate_by = 5
    context_object_name = 'item'

    def get_queryset(self):
        descripcion = self.request.GET.get('q', None)
        dt = "%s" % descripcion
        d_list = dt.split("*")
        q = d_list

        q_objects = []

        for item in q:
            q_objects.append(Q(descripcion__icontains=item))
            q_objects.append(Q(codigo_item__icontains=item))
            q_objects.append(Q(codigo_fabrica__icontains=item))
            q_objects.append(Q(carac_especial_1__icontains=item))
            q_objects.append(Q(carac_especial_2__icontains=item))

        query = reduce(operator.or_, q_objects)

        # query = reduce(operator.and_, (Q(descripcion__icontains=item) for item in q))
        r = self.model.objects.filter(query)

        # if r:
        #     query2 = query
        #     print 'entrooooo'
        # else:
        #     query2 = reduce(operator.and_, (Q(codigo_item__icontains=item) for item in q))

        if (descripcion):
            object_list = self.model.objects.filter(query, empresa=self.request.user.empresa)
        elif (descripcion == '*'):
            object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('pk')
        else:
            object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('pk')
        return object_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListarItem, self).dispatch(*args, **kwargs)


class DetalleItem(DetailView):
	template_name = 'producto/detalle_item.html'
	model = Item
	context_object_name = 'item'


class EditItem(UpdateView):
    template_name = 'producto/update.html'
    model = Item
    fields = ['codigo_item','codigo_fabrica','almacen','grupo','subgrupo',
    'descripcion','carac_especial_1','carac_especial_2','cantidad',
    'saldo_min','proveedor','imagen','unidad_medida','costo_unitario','precio_unitario']
    success_url = reverse_lazy('listar_item')


class DeleteItem(DeleteView):
	model = Item
	success_url = reverse_lazy('listar_item')


def eliminar(request, id):
	p = Item.objects.get(id=id)
	p.delete()
	return HttpResponseRedirect(reverse_lazy('listar_item'))


#====== views for import archivo of excel ======
class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean(self):
    	data = super(UploadFileForm, self).clean()

    	if 'file' not in data:
        	raise forms.ValidationError('')

        docfile = data['file']
    	extension = os.path.splitext(docfile.name)[1]

    	if not (extension in IMPORT_FILE_TYPES):
        	raise forms.ValidationError(u'%s no es un archivo válido. Por favor, asegúrese de que su archivo de entrada tenga la extension .xls' % docfile.name)


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        # if request.FILES:
        # 	datos=request.FILES['file']
        # 	filename = datos._name
        # 	print filename
        # 	fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
        # 	rute= '%s/%s' % (MEDIA_ROOT, datos)
        # 	for chunk in datos.chunks() :
        # 		fd.write(chunk)
        # 	fd.close()

        # 	dt=pe.get_sheet(file_name='%s' % (rute), name_columns_by_row=0)
        # 	yy=list(dt.colnames)
        # 	print yy
        today = date.today()

        def choice_func(row):
            cod = Proveedor.objects.filter(codigo=row[10])[0]
            row[10] = cod
            row.append(request.user)
            return row

        if form.is_valid():

            print 'ssssssssssssssssssssssssssssssss'
            # arryadates=['codigo_item', 'codigo_fabrica', 'almacen','grupo', 'subgrupo', 'descripcion', 'carac_especial_1', 'carac_especial_2', 'cantidad', 'saldo_min', 'proveedor', 'imagen', 'unidad_medida', 'costo_unitario', 'precio_unitario']
            datos = request.FILES['file']

            # datos2= pe.get_sheet(file_name='%s' % (datos),name_columns_by_row=0)
            # print(list(datos2.colnames))

            # for i in arryadates:
            # 	if i in dt:
            # 		print i
            # 	else:
            # 		print 'falseeeeeeee'

         #    for d in datos2:
        	# print d['codigo_item']
            # print request.FILES['file'].get_sheet()
            filename = datos._name
            fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
            print fd

            for chunk in datos.chunks():
                fd.write(chunk)
            fd.close()

            rute = '%s/%s' % (MEDIA_ROOT, datos)
            book = xlrd.open_workbook(rute)
            sheet = book.sheet_by_name('Sheet1')

            # wb = xlrd.open_workbook(rute)
            # ws = wb.sheet_by_name('Sheet1')
            # for i in range(ws.nrows):
            #     for j in range(ws.ncols):
            #         if ws.cell_type(i, j) != xlrd.XL_CELL_EMPTY:
            #             print ("  (%d, %d):%s:%s" % (i, j, ws.cell_type(i, j), ws.cell_value(i, j)))
            #         else:
            #             print "error"

            try:
                errores = []
                for r in range(1, sheet.nrows):

                    if  Item.objects.filter(codigo_item=sheet.cell(r, 0).value, empresa=request.user.empresa):
                        errores.append('* el codigo_item "%s" ya existe' % (sheet.cell(r, 0).value))

                    if sheet.cell_type(r, 8) != xlrd.XL_CELL_NUMBER:
                        errores.append('* cantidad "%s" tiene que ser numerico' % (sheet.cell(r, 8).value))

                    if sheet.cell_type(r, 9) != xlrd.XL_CELL_NUMBER:
                        errores.append('* saldo_min "%s" tiene que ser numerico' % (sheet.cell(r, 9).value))

                    if sheet.cell_type(r, 11) != xlrd.XL_CELL_TEXT:
                        errores.append('* imagen "%s" tiene que ser texto' % (sheet.cell(r, 11).value))

                    if not Proveedor.objects.filter(codigo=sheet.cell(r, 10).value, empresa=request.user.empresa):
                        errores.append('* el proveedor "%s" no existe en la base de datos' % (sheet.cell(r, 10).value))

                    if sheet.cell_type(r, 13) != xlrd.XL_CELL_NUMBER:
                        errores.append('* costo_unitario "%s" tiene que ser numerico' % (sheet.cell(r, 13).value))

                    if sheet.cell_type(r, 14) != xlrd.XL_CELL_NUMBER:
                        errores.append('* precio_unitario "%s" tiene que ser numerico' % (sheet.cell(r, 14).value))

                for s in range(1, sheet.nrows):

                    if errores:
                        for err in errores:
                            messages.error(request, err)
                            # messages.error(request, ', '.join([str(x) for x in errores]))
                        return render_to_response(
                        'producto/upload_form.html',
                        {
                            'form': form,
                        },
                        context_instance=RequestContext(request))
                    else:

                        crearItem = Item(
                            codigo_item=sheet.cell(s, 0).value,
                            codigo_fabrica=sheet.cell(s, 1).value,
                            almacen=sheet.cell(s, 2).value,
                            grupo=sheet.cell(s, 3).value,
                            subgrupo=sheet.cell(s, 4).value,
                            descripcion=sheet.cell(s, 5).value,
                            carac_especial_1=sheet.cell(s, 6).value,
                            carac_especial_2=sheet.cell(s, 7).value,
                            cantidad=sheet.cell(s, 8).value,
                            saldo_min=sheet.cell(s, 9).value,
                            proveedor=Proveedor.objects.get(codigo=sheet.cell(s, 10).value),
                            imagen=sheet.cell(s, 11).value,
                            unidad_medida=sheet.cell(s, 12).value,
                            costo_unitario=decimal.Decimal(sheet.cell(s, 13).value),
                            precio_unitario=decimal.Decimal(sheet.cell(s, 14).value),
                            empresa=request.user.empresa,
                        )
                        crearItem.save()

                        crearMovimiento = Movimiento(
                            cantidad=sheet.cell(s, 8).value,
                            precio_unitario=decimal.Decimal(sheet.cell(s, 14).value),
                            detalle='Saldo Inicial',
                            fecha_transaccion=date.today(),
                            motivo_movimiento='inicial',
                            item=crearItem,
                            empresa=request.user.empresa,
                        )
                        crearMovimiento.save()

                # try:

                # request.FILES['file'].save_book_to_database(
                #     models=[Item],
                #     initializers=[choice_func],
                #     mapdicts=[['codigo_item', 'codigo_fabrica', 'almacen', 'grupo', 'subgrupo', 'descripcion', 'carac_especial_1', 'carac_especial_2', 'cantidad', 'saldo_min', 'proveedor', 'imagen', 'unidad_medida', 'costo_unitario', 'precio_unitario', 'user']]
                # )

                messages.success(request, "Los datos se importaron correctamente")

                # filename = datos._name
                # # print filename

                # fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')

                # for chunk in datos.chunks() :
                #     fd.write(chunk)
                # fd.close()


                return HttpResponseRedirect(reverse_lazy('listar_item'))

            except Exception, e:
	        	messages.error(request, e)


    else:
        form = UploadFileForm()
    return render_to_response(
        'producto/upload_form.html',
        {
            'form': form,
        },
        context_instance=RequestContext(request))


