from django.shortcuts import render
from django.views.generic import CreateView,FormView
from .forms import CreateForm

# Create your views here.
class CrearProveedor(FormView):
	template_name = "proveedores/create.html"
	form_class = CreateForm

	def form_valid(self, form):
        	form.save()
        	return super(CrearProveedor, self).form_valid(form)
	
		
