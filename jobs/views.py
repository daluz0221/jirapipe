from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .modules import get_incidents

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
       
        incidencias = get_incidents("all")
        ctx["user_incidencias"] = incidencias
        
        return ctx
    