from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, FormView, CreateView, RedirectView, View, ListView, UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserForm, UserFormedit, reset_form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from apps.inicio.roles import *
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.models import User
from pure_pagination.mixins import PaginationMixin

# Create your views here.


class Inicio(TemplateView):
    template_name = "inicio/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Inicio, self).dispatch(*args, **kwargs)


class Index(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return HttpResponseRedirect(reverse_lazy('inicio'))  


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


class Reportes(TemplateView):
    template_name = 'inicio/reportes.html'

@has_role_decorator('adminstrador')
def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            rol = user_form.cleaned_data['rol']

            if rol == 'administrador':
                Administrador.assign_role_to_user(user)
            else:
                Operador.assign_role_to_user(user)

            # profile.user = user
            return HttpResponseRedirect(reverse_lazy('list_user'))
            registered = True

        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('inicio/register.html', {'user_form': user_form, 'registered': registered}, context)


class ListarUsuario(PaginationMixin, ListView):
    template_name = 'inicio/listar_usuarios.html'
    paginate_by = 5
    model = User
    context_object_name = 'users'

    def get_queryset(self):

        username = self.request.GET.get('q', None)

        if (username):
            object_list = self.model.objects.filter(username__icontains = username).order_by('pk')
        else:
            object_list = self.model.objects.all().order_by('pk')
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
        print user.password
        if request.method == "POST":

            form = UserFormedit(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                # post.author = request.user
                user.save()
                rol = form.cleaned_data['rol']

                if rol == 'administrador':
                    Administrador.assign_role_to_user(user)
                else:
                    Operador.assign_role_to_user(user)

                return HttpResponseRedirect(reverse_lazy('list_user'))

        return render(request, 'inicio/update.html', {'user_form': form, 'usere': user})


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
