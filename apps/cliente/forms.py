# -*- coding: utf-8 -*-
from django import forms
from .models import Cliente
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class ClienteForm(forms.Form):
	codigo = forms.CharField(max_length=50)
	razonsocial = forms.CharField(max_length=50)
	nit = forms.IntegerField()
	direccion = forms.CharField(max_length=50)
	telefonos1 = forms.CharField(
		max_length=8,
		validators=[
			RegexValidator(
				r'^[0-9]*$',
				'solo se admiten numeros',
				'numero invalido'
			),
			MinLengthValidator(7),
			MaxLengthValidator(8),
		],
	)
	telefonos2 = forms.CharField(
		max_length=8,
		required=False,
		validators=[
			RegexValidator(
				r'^[0-9]*$',
				'solo se admiten numeros',
				'numero invalido'
			),
			MinLengthValidator(7),
			MaxLengthValidator(8),
		],
	)
	telefonos3 = forms.CharField(
		max_length=8,
		required=False,
		validators=[
			RegexValidator(
				r'^[0-9]*$',
				'solo se admiten numeros',
				'numero invalido'
			),
			MinLengthValidator(7),
			MaxLengthValidator(8),
		],
	)
	contacto = forms.CharField(max_length=50)
	rubro = forms.CharField(max_length=50)
	categoria = forms.CharField(max_length=50)
	ubucaciongeo = forms.CharField(max_length=50) 
	fecha = forms.DateField()
	fecha2 = forms.DateField()
	textos = forms.CharField(max_length=50, required=False)
	textos2 = forms.CharField(max_length=50, required=False)

	class Meta:
		model = Cliente