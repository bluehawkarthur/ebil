from django import forms, http
from apps.proveedores.models import Proveedor
from .models import Item

from django.forms import ModelForm

class ItemForm(forms.Form):
	codigo_item = forms.CharField(max_length=50)
	codigo_fabrica = forms.CharField(max_length=50, required=False)
	almacen = forms.IntegerField()
	grupo = forms.CharField(max_length=50, required=False)
	subgrupo = forms.CharField(max_length=50, required=False)
	descripcion = forms.CharField(max_length=200)
	carac_especial_1 = forms.CharField(max_length=50, required=False)
	carac_especial_2 = forms.CharField(max_length=50, required=False)
	cantidad = forms.IntegerField()
	saldo_min = forms.IntegerField()
	proveedor = forms.ModelChoiceField(queryset='', empty_label='seleccione', required=False)
	imagen = forms.ImageField(required=False)
	unidad_medida = forms.CharField(max_length=20, required=False)
	costo_unitario = forms.DecimalField()
	precio_unitario = forms.DecimalField()

	class Meta:
		model = Item
