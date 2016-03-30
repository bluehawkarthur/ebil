# -*- coding: utf-8 -*-
from django import forms
from .models import Cliente
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class ClienteForm(forms.Form):
	codigo = forms.CharField(max_length=50)
	razonsocial = forms.CharField(max_length=50)
	nit = forms.IntegerField()
	direccion = forms.CharField(max_length=50, required=False)
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
		required=False,
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
	contacto = forms.CharField(max_length=50, required=False)
	rubro = forms.CharField(max_length=50, required=False)
	categoria = forms.CharField(max_length=50, required=False)
	ubucaciongeo = forms.CharField(max_length=50, label='Ubicacion geografica', required=False)
	fecha = forms.DateField(required=False)
	fecha2 = forms.DateField(required=False)
	textos = forms.CharField(max_length=50, required=False)
	textos2 = forms.CharField(max_length=50, required=False)

	class Meta:
		model = Cliente

	def clean_nit(self):
		try:
			Cliente.objects.get(nit=self.cleaned_data['nit'])
		except Cliente.DoesNotExist:
			return self.cleaned_data['nit']

		raise forms.ValidationError("este nit ya existe")

	def clean_codigo(self):
		try:
			Cliente.objects.get(codigo=self.cleaned_data['codigo'])
		except Cliente.DoesNotExist:
			return self.cleaned_data['codigo']

		raise forms.ValidationError("este codigo ya existe")
