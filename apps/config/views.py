from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.users.models import Personajuridica
from .forms import PersonajuridicaForm, EmpresaFormedit, DatosDosificacionForm
from .models import DatosDosificacion
from pure_pagination.mixins import PaginationMixin
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from django.contrib import messages


class Configuraciones(TemplateView):
    template_name = 'config/config.html'


def Createpersojuridica(request):
    if request.method == 'POST':
        form = PersonajuridicaForm(request.POST)
        if form.is_valid():
            personajurid = Personajuridica(
                razon_social=form.cleaned_data['razon_social'],
                nit=form.cleaned_data['nit'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                telefono2=form.cleaned_data['telefono2'],
                telefono3=form.cleaned_data['telefono3'],
                departamento=form.cleaned_data['departamento'],
                municipios=form.cleaned_data['municipios'])
            personajurid.save()
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

        form = EmpresaFormedit(request.POST, instance=empresa)
        if form.is_valid():
            user = form.save(commit=False)
            # user.empresa = form.cleaned_data['empresa']
            user.save()
            messages.success(request, "Los datos se guardaron correctamente")

    return render(request, 'config/empresa.html', {'form': form, 'empresa': empresa})


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
              'telefono2', 'telefono3', 'departamento', 'municipios']
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
            object_list = self.model.objects.filter(empresa=self.request.user.empresa).order_by('-pk')
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