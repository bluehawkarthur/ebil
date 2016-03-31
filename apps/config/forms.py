from django import forms
from apps.users.models import Personajuridica
from .models import Formatofactura


class PersonajuridicaForm(forms.Form):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False, label="Logo")


class EmpresaFormedit(forms.ModelForm):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.CharField(required=False)
    telefono3 = forms.CharField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False, label="Logo")

    class Meta:
        model = Personajuridica
        fields = ('razon_social', 'nit', 'direccion', 'telefono', 'departamento', 'municipios', 'logo')


class DatosDosificacionForm(forms.Form):
    nro_conrelativo = forms.IntegerField()
    fecha = forms.DateField(label="Fecha limite de emision")
    nro_autorizacion = forms.IntegerField()
    llave_digital = forms.CharField()


class FormatofacturaForm(forms.ModelForm):
    formato = forms.CharField(max_length=100)
    impresion = forms.CharField(max_length=100)
    facturacion = forms.CharField(max_length=100)
    tamanio = forms.CharField(max_length=100)
    frases_titulo = forms.CharField(max_length=100)
    frases_subtitulo = forms.CharField(max_length=100)
    frases_pie = forms.CharField(max_length=2100)

    class Meta:
        model = Formatofactura
        fields = ('formato', 'impresion', 'facturacion', 'tamanio', 'frases_titulo', 'frases_subtitulo', 'frases_pie')


class SucursalForm(forms.Form):
    nombre_sucursal = forms.CharField(max_length=100)
    nro_sucursal = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    telefono1 = forms.IntegerField()
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)