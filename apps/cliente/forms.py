from django import forms, http
from .models import Cliente

from django.forms import ModelForm

class ClienteForm(forms.Form):
	codigo = forms.CharField(max_length=50)
	razonsocial = forms.CharField(max_length=50)
	nit = forms.IntegerField()
	direccion = forms.CharField(max_length=50)
	telefonos1 = forms.IntegerField()
	telefonos2 = forms.IntegerField()
	telefonos3 = forms.IntegerField()
	contacto = forms.CharField(max_length=50)
	rubro = forms.CharField(max_length=50)
	categoria = forms.CharField(max_length=50)
	ubucaciongeo = forms.CharField(max_length=50) 
	fecha = forms.DateField()
	fecha2 = forms.DateField()
	textos = forms.CharField(max_length=50)
	textos2 = forms.CharField(max_length=50)

	class Meta:
		model = Cliente