from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, FormView, CreateView, RedirectView, View, ListView, UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserForm, UserFormedit, reset_form, RolForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from apps.inicio.roles import *
from rolepermissions.decorators import has_role_decorator
from rolepermissions.verifications import has_role
# from django.contrib.auth.models import User
from pure_pagination.mixins import PaginationMixin
from .models import Rol
from django.conf import settings
from apps.users.models import User
from django.core.management import call_command
# Create your views here.


class Inicio(TemplateView):
    template_name = "inicio/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Inicio, self).dispatch(*args, **kwargs)


class InicioRoot(TemplateView):
    template_name = "inicio/root.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InicioRoot, self).dispatch(*args, **kwargs)


class Index(View):

    def get(self, request, *args, **kwargs):

        #========= comamdo para hacer copias de seguridad de la base de datos ======
        # ==========================================================================
        output = open('output_filename.json','w')
        call_command('dumpdata',format='json',indent=3,stdout=output)
        output.close()
        # ==========================================================================
        # para restaurar la base de datos modificar el codigo
        #        loaddata

        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse_lazy('inicio_root'))
            else:
                return HttpResponseRedirect(reverse_lazy('inicio'))


class LoginView(FormView):
    form_class = LoginForm
    template_name = "inicio/login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'index'
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class Reportes(TemplateView):
    template_name = 'inicio/reportes.html'

# @has_role_decorator('administrador')
def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(request.POST, request.FILES)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.empresa = user_form.cleaned_data['empresa']
            user.set_password(user.password)
            user.save()
          
            rol = user_form.cleaned_data['rol']

            if rol == 'administrador':
                Administrador.assign_role_to_user(user)
                create1 = Rol(user=user, modelos='almacenes', operar=True, crear=True, editar=True, eliminar=True)
                create2 = Rol(user=user, modelos='clientes', operar=True, crear=True, editar=True, eliminar=True)
                create3 = Rol(user=user, modelos='proveedores', operar=True, crear=True, editar=True, eliminar=True)
                create4 = Rol(user=user, modelos='reportes', operar=True, crear=True, editar=True, eliminar=True)
                create5 = Rol(user=user, modelos='compras', operar=True, crear=True, editar=True, eliminar=True)
                create6 = Rol(user=user, modelos='usuarios', operar=True, crear=True, editar=True, eliminar=True)
                create7 = Rol(user=user, modelos='bancarizacion', operar=True, crear=True, editar=True, eliminar=True)
                create8 = Rol(user=user, modelos='configuracion', operar=True, crear=True, editar=True, eliminar=True)
                create8 = Rol(user=user, modelos='configuracion', operar=True, crear=True, editar=True, eliminar=True)
                create9 = Rol(user=user, modelos='facturacion', operar=True, crear=True, editar=True, eliminar=True)

                rol_list = [create1, create2, create3, create4, create5, create6, create7, create8, create9]

                for rol in rol_list:
                    rol.save()

                return HttpResponseRedirect(reverse_lazy('list_user'))
            else:
                Operador.assign_role_to_user(user)

                create1 = Rol(user=user, modelos='almacenes', operar=False, crear=False, editar=False, eliminar=False)
                create2 = Rol(user=user, modelos='clientes', operar=False, crear=False, editar=False, eliminar=False)
                create3 = Rol(user=user, modelos='proveedores', operar=False, crear=False, editar=False, eliminar=False)
                create4 = Rol(user=user, modelos='reportes', operar=False, crear=False, editar=False, eliminar=False)
                create5 = Rol(user=user, modelos='compras', operar=False, crear=False, editar=False, eliminar=False)
                create6 = Rol(user=user, modelos='usuarios', operar=False, crear=False, editar=False, eliminar=False)
                create7 = Rol(user=user, modelos='bancarizacion', operar=False, crear=False, editar=False, eliminar=False)
                create8 = Rol(user=user, modelos='configuracion', operar=False, crear=False, editar=False, eliminar=False)
                create9 = Rol(user=user, modelos='facturacion', operar=False, crear=False, editar=False, eliminar=False)

                rol_list = [create1, create2, create3, create4, create5, create6, create7, create8, create9]

                for rol in rol_list:
                    rol.save()
                return HttpResponseRedirect(reverse_lazy('permisos_user', kwargs={'pk':user.pk}))

            registered = True

        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('inicio/register.html', {'user_form': user_form, 'registered': registered}, context)


class ListarUsuario(PaginationMixin, ListView):
    template_name = 'inicio/listar_usuarios.html'
    paginate_by = 10
    model = User
    context_object_name = 'users'

    def get_queryset(self):

        username = self.request.GET.get('q', None)
        if self.request.user.is_superuser:
            if (username):
                object_list = self.model.objects.filter(username__icontains = username).order_by('pk')
            else:
                object_list = self.model.objects.all().order_by('pk')
        else:
            if (username):
                object_list = self.model.objects.filter(username__icontains = username, empresa=self.request.user.empresa.pk).order_by('pk')
            else:
                object_list = self.model.objects.filter(empresa=self.request.user.empresa.pk).order_by('pk')
                print 'llego'
        return object_list

@has_role_decorator('adminstrador')
def eliminar(request, id):
    p = User.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse_lazy('list_user'))


class EditUser(UpdateView):
    template_name = 'inicio/update.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('listar_item')

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


def user_edit(request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserFormedit()
    
        if request.method == "POST":

            form = UserFormedit(request.POST, request.FILES, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                # post.author = request.user
                user.empresa = form.cleaned_data['empresa']
                user.save()
                rol = form.cleaned_data['rol']

                roles = Rol.objects.filter(user=user)

                if rol == 'administrador':
                   
                    for r in roles:
                        r.operar = True
                        r.crear = True
                        r.editar = True
                        r.eliminar = True
                        r.save()
                    Administrador.assign_role_to_user(user)
                    return HttpResponseRedirect(reverse_lazy('list_user'))
                else:
                    if not has_role(user, [Operador]):
                        for r in roles:
                            r.operar = False
                            r.crear = False
                            r.editar = False
                            r.eliminar = False
                            r.save()
                            Operador.assign_role_to_user(user)
                        return HttpResponseRedirect(reverse_lazy('permisos_user', kwargs={'pk':user.pk}))

                    return HttpResponseRedirect(reverse_lazy('list_user'))


        return render(request, 'inicio/update.html', {'user_form': form, 'usere': user})


def user_permisos(request, pk):
        # user = get_object_or_404(User, pk=pk)
        # form = UserFormedit()
        # print user.password
        if request.method == "POST":

            formset = RolForm(request.POST, queryset=Rol.objects.filter(user=pk))
            if formset.is_valid():
                for form in formset.forms:
                    user = form.save(commit=False)
                    user.save()

            return HttpResponseRedirect(reverse_lazy('list_user'))
        else:
            formset = RolForm(queryset=Rol.objects.filter(user=pk))

        return render(request, 'inicio/edit_inline.html', {'formset': formset})



def change_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = reset_form(request.POST)
        if form.is_valid():
            newpassword = form.cleaned_data['newpassword1']
            user.set_password(newpassword)
            user.save()
            return HttpResponseRedirect(reverse_lazy('list_user'))

    else:
        form = reset_form()
    content = RequestContext(request, {'form': form, 'user_data': user})
    return render(request, 'inicio/reset_password.html', content,)


def perfil(request):
    user = get_object_or_404(User, pk=request.user.pk)

    return render(request, 'inicio/perfil.html', {'usere': user})
