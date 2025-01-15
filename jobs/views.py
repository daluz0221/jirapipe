from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .models import Incidencias
from .modules import get_incidents, get_history_user, get_tareas


class MyLoginRequiredView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'


class CreateLoginRequiredView(LoginRequiredMixin, CreateView):
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
        ctx["user_histories"] = incidencias.get("history_list")
        ctx["parent_incidence"] = incidencias.get("incidencia_dict")
        
        return ctx


class TareasView(MyLoginRequiredView):
    template_name = "jobs/tareas_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(TareasView, self).get_context_data(**kwargs)

        history_user_slug = self.kwargs.get("history_user_slug")
       
        incidencias = get_tareas("all", history_user_slug)
        ctx["parent_history_user"] = incidencias.get("history_user_dict")
        ctx["tareas"] = incidencias.get("tareas_list")
        
        return ctx


class CreateIncidenceView(CreateLoginRequiredView):

    template_name = "home.html"
    model = Incidencias
    fields = "__all__"
    context_object_name = "create_incidence_form"

    def form_invalid(self, form):
        return JsonResponse({
            "success": False,
            "errors": form.errors,
        }, status=400)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            "success": True,
            "id": self.object.id, 
            "titulo": self.object.title
        })