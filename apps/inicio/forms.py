# -*- coding: utf-8 -*-
from django import forms, http
# from captcha.fields import CaptchaField
# from captcha.fields import ReCaptchaField
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django.contrib.auth.forms import AuthenticationForm
import socket
from django.contrib.auth.models import User
from .models import Rol
from django.forms import modelformset_factory


REMOTE_SERVER = "www.google.com"
def is_connected():
	try:
	    # see if we can resolve the host name -- tells us if there is
	    # a DNS listening
	    host = socket.gethostbyname(REMOTE_SERVER)
	    # connect to the host -- tells us if the host is actually
	    # reachable
	    s = socket.create_connection((host, 80), 2)
	    print "conectado"
	    return True
	except:
		pass
		return False
		print is_connected()

class LoginForm(AuthenticationForm):
    # captcha = CaptchaField()
    pass
    # if is_connected():
    # 	captcha = NoReCaptchaField()
    # else:
    # 	pass

list_of_choices = (
	('', '-- seleccionar --'),
    ('administrador', 'Administrador'),
    ('operador', 'Operador'),
)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=30, render_value=False)), label="Contraseña (confirmación):")
    rol = forms.ChoiceField(choices=list_of_choices)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Los dos campos de contraseña no coinciden.")
        return self.cleaned_data


class UserFormedit(forms.ModelForm):
    
    rol = forms.ChoiceField(choices=list_of_choices)

    class Meta:
        model = User
        fields = ('username',)


class reset_form(forms.Form):
    newpassword1 = forms.CharField(max_length=20, label="Contraseña", widget=forms.TextInput(attrs={'type':'password',  'class' : 'span'}))
    newpassword2 = forms.CharField(max_length=20, label="Contraseña (de nuevo)", widget=forms.TextInput(attrs={'type':'password',  'class' : 'span'}))

    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError("Los dos campos de contraseña no coinciden.")
        return self.cleaned_data


RolFormSet = modelformset_factory(Rol, extra=0, fields=('modelos', 'crear', 'editar', 'eliminar' ))


class RolForm(RolFormSet):

    def add_fields(self, form, index):

        super(RolForm, self).add_fields(form, index)
        form.fields['modelos'] = forms.CharField(required=False)
        form.fields['modelos'].widget.attrs['disabled'] = True
        form.fields['crear'] = forms.BooleanField(required=False)
        form.fields['editar'] = forms.BooleanField(required=False)

