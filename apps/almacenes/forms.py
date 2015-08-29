from django import forms, http
from apps.proveedores.models import Proveedor

from django.forms import ModelForm

class ItemForm(forms.Form):
	codigo_item = forms.CharField(max_length=10)
	codigo_fabrica = forms.CharField(max_length=10)
	almacen = forms.IntegerField()
	grupo = forms.CharField(max_length=50)
	subgrupo = forms.CharField(max_length=50)
	descripcion = forms.CharField(max_length=200)
	carac_especial_1 = forms.CharField(max_length=50)
	carac_especial_2 = forms.CharField(max_length=50)
	cantidad = forms.IntegerField()
	saldo_min = forms.IntegerField()
	proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), empty_label='seleccione')
	imagen = forms.ImageField()
	unidad_medida = forms.CharField(max_length=20)
	costo_unitario = forms.DecimalField(max_digits=5, decimal_places=3)

	#proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), empty_label='seleccione')

		
