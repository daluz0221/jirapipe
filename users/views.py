from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from django.views.generic import (
    View,
    CreateView
)

from django.views.generic.edit import (
    FormView
)

from .forms import UserRegisterForm, LoginForm
from .models import User
# Create your views here.





class UserManageView(View):
    template_name = "users/login.html"

    def get(self, request):
        form_registro = UserRegisterForm()
        form_login = LoginForm()

        return render(request, self.template_name, {
            "form_registro": form_registro,
            "form_login": form_login
        })

    def post(self, request):
        if "form_registro" in request.POST:
            form_registro = UserRegisterForm(request.POST)
            if form_registro.is_valid():
                

                return redirect("home")


class UserRegisterView(FormView):
    template_name = "users/login.html"
    form_class = UserRegisterForm
    success_url = '/'
    context_object_name = "register_form"

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data.get("username"),
            form.cleaned_data.get("email"),
            form.cleaned_data.get("names"),
            form.cleaned_data.get("lastnames"),
            form.cleaned_data.get("password1"),

        )

        return super(UserRegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('controller:home')
    context_object_name = "login_form"

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        login(self.request, user)

        return super(LoginView, self).form_valid(form)
    

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                "controller:home"
            )
        )