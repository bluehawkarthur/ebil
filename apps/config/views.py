# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse_lazy
from apps.users.models import Personajuridica
from .forms import PersonajuridicaForm, EmpresaFormedit, DatosDosificacionForm, FormatofacturaForm, SucursalForm
from .models import DatosDosificacion, Formatofactura, AlmacenesCampos, ProveedoresCampos, ClienteCampos, FacturaCampos, Sucursal
from apps.cliente.models import Cliente
from pure_pagination.mixins import PaginationMixin
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from django.contrib import messages
from django.core.management import call_command
from datetime import date
from ebil.settings import MEDIA_ROOT
from django import forms
import os
IMPORT_FILE_TYPES = ['.json', ]


class Configuraciones(TemplateView):
    template_name = 'config/config.html'


def Createpersojuridica(request):
    if request.method == 'POST':
        form = PersonajuridicaForm(request.POST, request.FILES)
        if form.is_valid():
            personajurid = Personajuridica(
                razon_social=form.cleaned_data['razon_social'],
                nit=form.cleaned_data['nit'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                telefono2=form.cleaned_data['telefono2'],
                telefono3=form.cleaned_data['telefono3'],
                departamento=form.cleaned_data['departamento'],
                municipios=form.cleaned_data['municipios'],
                logo=form.cleaned_data['logo'])
            personajurid.save()
            formatofact = Formatofactura(
                formato='general',
                impresion='vacia',
                facturacion='normal',
                tamanio='oficio',
                frases_titulo='Factura',
                frases_subtitulo='Derecho a Credito Fiscal',
                frases_pie='Ley N° 453: Si se te ha vulnerado algún derecho puedes exigir la reposición o restauración.',
                empresa=personajurid
            )
            formatofact.save()
            campo_item = AlmacenesCampos(
                codigo_fabr_usar=True,
                codigo_fabr_reque=False,
                codigo_fabricatipo='',
                codigo_fabricacaractr=20,
                caract_espec_usar=True,
                caract_espec_requerid=False,
                caract_espectipo='',
                caract_especaractr=20,
                unidad_medid_usar=True,
                unidad_medid_requerido=False,
                unidad_medidatipo='',
                unidad_medidacaractr=15,
                imagen_usar=True,
                imagen_requer=False,
                grupo_usar=True,
                grupo_requerido=False,
                grupo_tipo='',
                grupo_caractr=20,
                subgrupo_usar=True,
                subgrupo_requerido=False,
                subgrupo_tipo='',
                subgrupo_caractr=20,
                carac_especial_2_usar=True,
                carac_especial_2_requerido=False,
                carac_especial_2_tipo='',
                carac_especial_2_caractr=20,
                empresa=personajurid
            )
            campo_item.save()
            campo_proveedor = ProveedoresCampos(
                direccion_usar=True,
                direccion_requerido=False,
                direccion_tipo='',
                direccion_caractr=20,
                telefonos1_usar=True,
                telefonos1_requerido=False,
                telefonos1_tipo='',
                telefonos1_caractr=7,
                telefonos2_usar=True,
                telefonos2_requerido=False,
                telefonos2_tipo='',
                telefonos2_caractr=7,
                telefonos3_usar=True,
                telefonos3_requerido=False,
                telefonos3_tipo='',
                telefonos3_caractr=7,
                contacto_usar=True,
                contacto_requerido=False,
                contacto_tipo='',
                contacto_caractr=20,
                rubro_usar=True,
                rubro_requerido=False,
                rubro_tipo='',
                rubro_caractr=15,
                ubicacion_geo_usar=True,
                ubicacion_geo_requerido=False,
                ubicacion_geo_tipo='',
                ubicacion_geo_caractr=15,
                fechas_usar=True,
                fechas_requerido=False,
                fechas2_usar=True,
                fechas2_requerido=False,
                textos_usar=True,
                textos_requerido=False,
                textos_tipo='',
                textos_caractr=15,
                textos2_usar=True,
                textos2_requerido=False,
                textos2_tipo='',
                textos2_caractr=15,
                empresa=personajurid
            )
            campo_proveedor.save()

            campo_cliente = ClienteCampos(
                direccion_usar=True,
                direccion_requerido=False,
                direccion_tipo='',
                direccion_caractr=15,
                telefono1_usar=True,
                telefono1_requerido=False,
                telefono1_tipo='',
                telefono1_caractr=7,
                telefono2_usar=True,
                telefono2_requerido=False,
                telefono2_tipo='',
                telefono2_caractr=7,
                telefono3_usar=True,
                telefono3_requerido=False,
                telefono3_tipo='',
                telefono3_caractr=7,
                contacto_usar=True,
                contacto_requerido=False,
                contacto_tipo='',
                contacto_caractr=15,
                rubro_usar=True,
                rubro_requerido=False,
                rubro_tipo='',
                rubro_caractr=15,
                categoria_usar=True,
                categoria_requerido=False,
                categoria_tipo='',
                categoria_caractr=15,
                ubicaciongeo_usar=True,
                ubicaciongeo_requerido=False,
                ubicaciongeo_tipo='',
                ubicaciongeo_caractr=15,
                fecha_usar=True,
                fecha_requerido=False,
                fecha2_usar=True,
                fecha2_requerido=False,
                texto_usar=True,
                texto_requerido=False,
                texto_tipo='',
                texto_caractr=15,
                texto2_usar=True,
                texto2_requerido=False,
                texto2_tipo='',
                texto2_caractr=15,
                empresa=personajurid
            )
            campo_cliente.save()
            return HttpResponseRedirect(reverse_lazy('listarPersonajuridica'))
            # render_to_response('config/createpersojuridica.html')
    else:
        form = PersonajuridicaForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('config/createpersojuridica.html', variables)


def Empresa(request):
    empresa = get_object_or_404(Personajuridica, pk=request.user.empresa.pk)
    form = EmpresaFormedit()

    if request.method == "POST":

        form = EmpresaFormedit(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            user = form.save(commit=False)
            # user.empresa = form.cleaned_data['empresa']
            user.save()
            messages.success(request, "Los datos se guardaron correctamente")
            return HttpResponseRedirect(reverse_lazy('index'))

    return render(request, 'config/empresa.html', {'form': form, 'empresa': empresa})


def Formatfactura(request):
    formato = get_object_or_404(
        Formatofactura, empresa=request.user.empresa.pk)

    form = FormatofacturaForm()

    if request.method == "POST":

        form = FormatofacturaForm(request.POST, instance=formato)
        if form.is_valid():
            user = form.save(commit=False)
            # user.empresa = form.cleaned_data['empresa']
            user.save()
            messages.success(request, "Los datos se guardaron correctamente")
            return HttpResponseRedirect(reverse_lazy('index'))

    return render(request, 'config/formato.html', {'form': form, 'formato': formato})


class ListarPersonajuridica(PaginationMixin, ListView):
    template_name = 'config/listarPersonajuridica.html'
    paginate_by = 5
    model = Personajuridica
    context_object_name = 'personajuridica'

    def get_queryset(self):

        razon_social = self.request.GET.get('q', None)
        if (razon_social):
            object_list = self.model.objects.filter(
                razon_social__icontains=razon_social).order_by('pk')
        else:
            object_list = self.model.objects.all().order_by('pk')
        return object_list


class EditPersonajuridica(UpdateView):
    template_name = 'config/edit_Personajuridica.html'
    model = Personajuridica
    fields = ['razon_social', 'nit', 'direccion', 'telefono',
              'telefono2', 'telefono3', 'departamento', 'municipios', 'logo']
    success_url = reverse_lazy('listarPersonajuridica')


class DetallePersonajuridica(DetailView):
    template_name = 'config/detalle_peronajurid.html'
    model = Personajuridica
    context_object_name = 'personajuridica'


def DeletePersonajuridica(request, personajuridica):
    e = Personajuridica.objects.get(id=personajuridica)
    e.delete()
    return HttpResponseRedirect(reverse_lazy('listarPersonajuridica'))


def CrearDatosDosificacion(request):
    if request.method == 'POST':
        form = DatosDosificacionForm(request.POST)
        if form.is_valid():
            datosdosificacion = DatosDosificacion(
                nro_conrelativo=form.cleaned_data['nro_conrelativo'],
                fecha=form.cleaned_data['fecha'],
                nro_autorizacion=form.cleaned_data['nro_autorizacion'],
                llave_digital=form.cleaned_data['llave_digital'],
                empresa=request.user.empresa,
                contador=0)

            datosdosificacion.save()
            return HttpResponseRedirect(reverse_lazy('lista_datosdosificacion'))
            # return render_to_response('config/creardatosDosificacion.html')
    else:
        form = DatosDosificacionForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('config/creardatosDosificacion.html', variables)


class ListarDatosDosificacion(PaginationMixin, ListView):
    template_name = 'config/lista_datosdosificacion.html'
    paginate_by = 5
    model = DatosDosificacion
    context_object_name = 'DatosDosificacion'

    def get_queryset(self):

        razon_social = self.request.GET.get('q', None)
        if (razon_social):
            object_list = self.model.objects.filter(
                razon_social__icontains=razon_social).order_by('-pk')
        else:
            object_list = self.model.objects.filter(
                empresa=self.request.user.empresa).order_by('-pk')
        return object_list


class DetalleDatosDosificacion(DetailView):
    template_name = 'config/detalle_datosdosificacion.html'
    model = DatosDosificacion
    context_object_name = 'DatosDosificacion'


class EditDatosDosificacion(UpdateView):
    template_name = 'config/edit_datosdosificacion.html'
    model = DatosDosificacion
    fields = ['nro_conrelativo', 'fecha', 'nro_autorizacion', 'llave_digital']
    success_url = reverse_lazy('lista_datosdosificacion')


def DeleteDatosDosificacion(request, datosdosificacion):
    e = DatosDosificacion.objects.get(id=datosdosificacion)
    e.delete()
    print e
    return HttpResponseRedirect(reverse_lazy('lista_datosdosificacion'))


def CrearFormatofactura(request):
    if request.method == 'POST':
        form = FormatofacturaForm(request.POST)
        if form.is_valid():
            formatofactura = Formatofactura(
                formato=form.cleaned_data['formato'],
                impresion=form.cleaned_data['impresion'],
                facturacion=form.cleaned_data['facturacion'],
                tamanio=form.cleaned_data['tamanio'],
                frases_titulo=form.cleaned_data['frases_titulo'],
                frases_subtitulo=form.cleaned_data['frases_subtitulo'],
                frases_pie=form.cleaned_data['frases_pie'])
            formatofactura.save()
            return HttpResponseRedirect(reverse_lazy('crearfacturaCampos'))
            # return render_to_response('config/crearFormatofactura.html')
    else:
        form = FormatofacturaForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('config/crearFormatofactura.html', variables)


def copiaBase(request):
    template_name = "config/copia_base.html"

    if request.method == 'POST':

        if 'copia' in request.POST:
            response = HttpResponse(content_type='text/plain; charset=utf-8')
            today = date.today()
            filename = 'copia_base' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.json'.format(filename)

            # response['Content-Disposition'] = 'attachment; filename="copia_base.json"'
            output = open('templates/config/output_filename.json', 'w')
            call_command('dumpdata', format='json', indent=3, stdout=output)
            output.close()
            t = loader.get_template('config/output_filename.json')

            response.write(t.render())

            return response

    return render(request, template_name)


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean(self):
        data = super(UploadFileForm, self).clean()

        if 'file' not in data:
            raise forms.ValidationError('')

        docfile = data['file']
        extension = os.path.splitext(docfile.name)[1]

        if not (extension in IMPORT_FILE_TYPES):
            raise forms.ValidationError(
                u'%s no es un archivo válido. Por favor, asegúrese de que su archivo tenga la extension .json' % docfile.name)


def import_base(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        if form.is_valid():

            datos = request.FILES['file']

            filename = datos._name
            fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
            print fd

            for chunk in datos.chunks():
                fd.write(chunk)
            fd.close()

            rute = '%s/%s' % (MEDIA_ROOT, datos)
            call_command('loaddata', rute)
            os.unlink(rute)
            messages.success(request, "Los datos se cargaron correctamente")
            return HttpResponseRedirect(reverse_lazy('index'))

    else:
        form = UploadFileForm()
    return render_to_response(
        'config/upload_base.html',
        {
            'form': form,
        },
        context_instance=RequestContext(request))


class EditAlmacenesCampos(UpdateView):
    template_name = 'config/edit_alamacen_campos.html'
    model = AlmacenesCampos
    fields = ['codigo_fabr_usar', 'codigo_fabr_reque', 'codigo_fabricatipo', 'codigo_fabricacaractr', 
    'caract_espec_usar', 'caract_espec_requerid', 'caract_espectipo', 'caract_especaractr', 
    'unidad_medid_usar', 'unidad_medid_requerido', 'unidad_medidatipo', 'unidad_medidacaractr', 'imagen_usar', 'imagen_requer', 'grupo_usar','grupo_requerido',
    'grupo_tipo', 'grupo_caractr', 'subgrupo_usar', 'subgrupo_requerido', 'subgrupo_tipo', 'subgrupo_caractr', 'carac_especial_2_usar',
    'carac_especial_2_requerido', 'carac_especial_2_tipo', 'carac_especial_2_caractr']
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return AlmacenesCampos.objects.get(empresa=self.request.user.empresa)


class EditProveedoresCampos(UpdateView):
    template_name = 'config/edit_proveedcamps.html'
    model = ProveedoresCampos
    fields = ['direccion_usar', 'direccion_requerido', 'direccion_tipo', 'direccion_caractr', 
    'telefonos1_usar', 'telefonos1_requerido', 'telefonos1_tipo', 'telefonos1_caractr', 'telefonos2_usar', 'telefonos2_requerido', 'telefonos2_tipo', 'telefonos2_caractr',
    'telefonos3_usar', 'telefonos3_requerido', 'telefonos3_tipo', 'telefonos3_caractr', 'contacto_usar', 'contacto_requerido', 'contacto_tipo', 'contacto_caractr', 
    'rubro_usar', 'rubro_requerido', 'rubro_tipo', 'rubro_caractr', 'ubicacion_geo_usar', 'ubicacion_geo_requerido', 'ubicacion_geo_tipo', 'ubicacion_geo_caractr', 
    'fechas_usar', 'fechas_requerido', 'fechas2_usar', 'fechas2_requerido', 'textos_usar', 'textos_requerido', 'textos_tipo', 'textos_caractr',
    'textos2_usar', 'textos2_requerido', 'textos2_tipo', 'textos2_caractr']
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return ProveedoresCampos.objects.get(empresa=self.request.user.empresa)


class EditClienteCampos(UpdateView):
    template_name = 'config/edit_clientcamp.html'
    model = ClienteCampos
    fields = ['direccion_usar', 'direccion_requerido','direccion_tipo', 'direccion_caractr', 
    'telefono1_usar', 'telefono1_requerido', 'telefono1_tipo', 'telefono1_caractr', 'telefono2_usar', 'telefono2_requerido', 'telefono2_tipo', 'telefono2_caractr', 
    'telefono3_usar', 'telefono3_requerido', 'telefono3_tipo', 'telefono3_caractr', 'contacto_usar', 'contacto_requerido', 'contacto_tipo', 'contacto_caractr', 
    'rubro_usar', 'rubro_requerido', 'rubro_tipo', 'rubro_caractr', 'categoria_usar', 'categoria_requerido', 'categoria_tipo', 'categoria_caractr', 
    'ubicaciongeo_usar', 'ubicaciongeo_requerido', 'ubicaciongeo_tipo', 'ubicaciongeo_caractr', 'fecha_usar', 'fecha_requerido', 'fecha2_usar', 'fecha2_requerido',
    'texto_usar', 'texto_requerido', 'texto_tipo', 'texto_caractr', 'texto2_usar', 'texto2_requerido', 'texto2_tipo', 'texto2_caractr']
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return ClienteCampos.objects.get(empresa=self.request.user.empresa)


class EditFacturaCampos(UpdateView):
    template_name = 'config/edit_factCamp.html'
    model = FacturaCampos
    fields = ['descuento_usar', 'descuento_requerido', 'recargo_usar', 'recargo_requerido',
    'ice_usar', 'ice_requerido', 'exentos_usar', 'exentos_requerido', 'tipos_venta_usar', 'tipos_venta_requerido']
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return FacturaCampos.objects.get(empresa=self.request.user.empresa)


def CreateSucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            sucursal = Sucursal(
                nombre_sucursal=form.cleaned_data['nombre_sucursal'],
                nro_sucursal=form.cleaned_data['nro_sucursal'],
                direccion=form.cleaned_data['direccion'],
                telefono1=form.cleaned_data['telefono1'],
                telefono2=form.cleaned_data['telefono2'],
                telefono3=form.cleaned_data['telefono3'],
                departamento=form.cleaned_data['departamento'],
                municipios=form.cleaned_data['municipios'],
                empresa=request.user.empresa)
            sucursal.save()
            return HttpResponseRedirect(reverse_lazy('inicio'))
            # return render_to_response('config/crearSucursal.html')
    else:
        form = SucursalForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('config/crearSucursal.html', variables)
