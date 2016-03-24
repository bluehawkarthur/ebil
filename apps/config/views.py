# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse_lazy
from apps.users.models import Personajuridica
from .forms import PersonajuridicaForm, EmpresaFormedit, DatosDosificacionForm, FormatofacturaForm
from .models import DatosDosificacion, Formatofactura, AlmacenesCampos
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
