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


class CrearItem(FormView):
	template_name = 'producto/crear_item.html'
	form_class = ItemForm
	success_url = reverse_lazy('listar_item')

	# personalize choices for user authenticate
	def get_form(self, form_class):
		form = form_class(**self.get_form_kwargs())
		form.fields['proveedor'].queryset = Proveedor.objects.filter(user=self.request.user.id).all()
		return form

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
			item.user = self.request.user
			item.save()
			today = date.today()
			movimiento = Movimiento()
			movimiento.cantidad = form.cleaned_data['cantidad']
			movimiento.precio_unitario = form.cleaned_data['precio_unitario']
			movimiento.detalle = 'Saldo Inicial'
			movimiento.fecha_transaccion = today.strftime('%Y-%m-%d')
			movimiento.motivo_movimiento = 'inicial'
			movimiento.item = item
			movimiento.save()
			return super(CrearItem, self).form_valid(form)



from rolepermissions.mixins import HasRoleMixin


import operator
from django.db.models import Q


class ListarItem(PaginationMixin, ListView):
	template_name = 'producto/listar_item.html'
	model = Item
	paginate_by = 5
	context_object_name = 'item'

	def get_queryset(self):

		descripcion = self.request.GET.get('q', None)
		dt = "%s" % descripcion
	
		d_list = dt.split("*")
		

		# resultado = []
		# if (descripcion):
		# 	for i in d_list:
		# 		object_list = self.model.objects.filter(descripcion__icontains = i).order_by('pk')
		# 		resultado.extend(object_list)
		# 		type(resultado)
		# elif (descripcion == '*'):
		# 	resultado = self.model.objects.all().order_by('pk')
		# else:
		# 	resultado = self.model.objects.all().order_by('pk')
		# return resultado
		# object_list = self.model.objects.filter(descripcion__icontains = i).order_by('pk')
		#///////////////////////////

		q = d_list
		print d_list
		query = reduce(operator.and_, (Q(descripcion__contains=item) for item in q))
		# result = User.objects.filter(query)

		if (descripcion):
			object_list = self.model.objects.filter(query)
			print object_list
		elif (descripcion == '*'):
			object_list = self.model.objects.all().order_by('pk')
		else:
			object_list = self.model.objects.all().order_by('pk')
		return object_list


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

            for r in range(1, sheet.nrows):
                print sheet.cell(r, 0).value
                crearItem = Item(
                    codigo_item=sheet.cell(r, 0).value,
                    codigo_fabrica=sheet.cell(r, 1).value,
                    almacen=sheet.cell(r, 2).value,
                    grupo=sheet.cell(r, 3).value,
                    subgrupo=sheet.cell(r, 4).value,
                    descripcion=sheet.cell(r, 5).value,
                    carac_especial_1=sheet.cell(r, 6).value,
                    carac_especial_2=sheet.cell(r, 7).value,
                    cantidad=sheet.cell(r, 8).value,
                    saldo_min=sheet.cell(r, 9).value,
                    proveedor=Proveedor.objects.get(codigo=sheet.cell(r, 10).value),
                    imagen=sheet.cell(r, 11).value,
                    unidad_medida=sheet.cell(r, 12).value,
                    costo_unitario=decimal.Decimal(sheet.cell(r, 13).value),
                    precio_unitario=decimal.Decimal(sheet.cell(r, 14).value),
                    user=request.user,
                )
                crearItem.save()



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

          #   except Exception, e:
	        	# messages.error(request, "error en el archivo por favor verifique q los datos sean correctos")



    else:
        form = UploadFileForm()
    return render_to_response(
        'producto/upload_form.html',
        {
            'form': form,
        },
        context_instance=RequestContext(request))


