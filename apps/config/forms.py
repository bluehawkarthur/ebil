from django import forms
from apps.users.models import Personajuridica


class PersonajuridicaForm(forms.Form):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)


class EmpresaFormedit(forms.ModelForm):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.CharField(required=False)
    telefono3 = forms.CharField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)

    class Meta:
        model = Personajuridica
        fields = ('razon_social', 'nit', 'direccion', 'telefono', 'departamento', 'municipios')


class DatosDosificacionForm(forms.Form):
    nro_conrelativo = forms.IntegerField()
    fecha = forms.DateField()
    nro_autorizacion = forms.IntegerField()
    llave_digital = forms.CharField()
