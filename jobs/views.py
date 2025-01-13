from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .modules import get_incidents, get_history_user


class MyLoginRequiredView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'


class HomeView(MyLoginRequiredView):
    template_name = "home.html"

   

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
       
        incidencias = get_incidents("all", self.request.user)
        ctx["user_incidencias"] = incidencias
        
        return ctx




class HistoryUserView(MyLoginRequiredView):
    template_name = "jobs/historias_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(HistoryUserView, self).get_context_data(**kwargs)

        incident = self.kwargs.get("incidencia_slug")
       
        incidencias = get_history_user("all", incident)
        ctx["user_histories"] = incidencias
        
        return ctx


