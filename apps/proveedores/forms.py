from django import forms, http

class CreateForm(forms.Form):
	codigo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'off'}))
	razon_social = forms.CharField(max_length=150)
	nit = forms.CharField(max_length=20)
	direccion = forms.CharField(max_length=50)
	telefono1 = forms.IntegerField(required=True)
	telefono2 = forms.IntegerField(required=False)
	telefono3 = forms.IntegerField(required=False)
	contactos = forms.CharField(max_length=150)
	rubro = forms.CharField(max_length=50)
	ubicacion_geo = forms.CharField(max_length=50)
	fecha1 = forms.DateField()
	fecha2 = forms.DateField()
	texto1 = forms.CharField(max_length=50)
	texto2 = forms.CharField(max_length=50)
