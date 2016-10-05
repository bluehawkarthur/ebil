from django import forms, http
from django.core.exceptions import NON_FIELD_ERRORS


class CreateForm(forms.Form):
    codigo = forms.CharField(max_length=20)
    razon_social = forms.CharField(max_length=150)
    nit = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=50, required=False)
    telefono1 = forms.IntegerField(required=False)
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    contactos = forms.CharField(max_length=150, required=False)
    rubro = forms.CharField(max_length=50, required=False)
    ubicacion_geo = forms.CharField(max_length=50, required=False)
    fecha1 = forms.DateField(required=False)
    fecha2 = forms.DateField(required=False)
    texto1 = forms.CharField(max_length=50, required=False)
    texto2 = forms.CharField(max_length=50, required=False)


    def clean(self):
        return self.cleaned_data
