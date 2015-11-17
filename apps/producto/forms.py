from django import forms, http
from apps.proveedores.models import Proveedor
from .models import Item

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
	proveedor = forms.ModelChoiceField(queryset='', empty_label='seleccione')
	imagen = forms.ImageField(required=False)
	unidad_medida = forms.CharField(max_length=20)
	costo_unitario = forms.DecimalField(max_digits=5, decimal_places=3)
	precio_unitario = forms.DecimalField(max_digits=5, decimal_places=3)

	class Meta:
		model = Item
