from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, RedirectView, View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm 

# Create your views here.
class Index(TemplateView):
	template_name= "inicio/index.html"

class Inicio(TemplateView):
	template_name= "inicio/inicio.html"

class LoginView(FormView):
    form_class = LoginForm
    template_name = "inicio/login.html"
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
    pattern_name = 'index'
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
