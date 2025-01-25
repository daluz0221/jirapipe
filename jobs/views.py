from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .forms import IncidenciaForm, HistoryUserForm, TareasForm
from .models import Incidencias
from .modules import get_incidents, get_history_user, get_tareas


class MyLoginRequiredView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'


class CreateLoginRequiredView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'


class UpdateLoginRequired(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("users_app:user_login")
    redirect_field_name = 'next'    





class HomeView(MyLoginRequiredView):
    template_name = "home.html"

   

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
       
        incidencias = get_incidents("all", self.request.user)
        ctx["user_incidencias"] = incidencias
        ctx["incidence_form"] = IncidenciaForm
        ctx["incidence_update_form"] = IncidenciaForm
        
        return ctx




class HistoryUserView(MyLoginRequiredView):
    template_name = "jobs/historias_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(HistoryUserView, self).get_context_data(**kwargs)

        incident = self.kwargs.get("incidencia_slug")
       
        incidencias = get_history_user("all", incident_slug=incident)
        ctx["user_histories"] = incidencias.get("history_list")
        ctx["parent_incidence"] = incidencias.get("incidencia_dict")
        ctx["history_user_form"] = HistoryUserForm
        
        return ctx


class TareasView(MyLoginRequiredView):
    template_name = "jobs/tareas_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(TareasView, self).get_context_data(**kwargs)

        history_user_slug = self.kwargs.get("history_user_slug")
        incident = self.kwargs.get("incidencia_slug")
       
        incidencia = get_incidents("one", self.request.user, slug=incident)
        incidencias = get_tareas("all", history_user_slug=history_user_slug)
        ctx["parent_history_user"] = incidencias.get("history_user_dict")
        ctx["parent_incidence"] = incidencia
        ctx["tareas"] = incidencias.get("tareas_list")
        ctx["tarea_form"] = TareasForm
        
        return ctx


class CreateIncidenceView(CreateLoginRequiredView):
    
    form_class = IncidenciaForm
    success_url = '.'
    template_name = 'jobs/create_incidence.html'


    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CreateHistoryUserView(CreateLoginRequiredView):
    
    form_class = HistoryUserForm
    success_url = '.'
    template_name = 'jobs/create_history_user.html'


    def form_valid(self, form):
      
        incidence_slug = self.kwargs.get("incidencia_slug")
        incidence = get_incidents("one", self.request.user, slug=incidence_slug)
        form.instance.incidencia = incidence
    
        return super().form_valid(form)




class CreateTareaView(CreateLoginRequiredView):
    
    form_class = TareasForm
    success_url = '.'
    template_name = 'jobs/create_tarea.html'


    def form_valid(self, form):
      
        huser_slug = self.kwargs.get("history_user_slug")
        hsuer = get_history_user("one", histoy_user_slug=huser_slug)
        form.instance.user_history = hsuer
    
        return super().form_valid(form)
    


class UpdateIncidenceView(UpdateLoginRequired):
    model = Incidencias
    fields = (
            'title',
            'description',
            'type',
            'progress',
            'priority',
            'due_date'
        )
    slug_url_kwarg = "incidence_slug" 
    template_name = "jobs/update_incidence.html"
    success_url = '.'





def get_data(request, slug):
    print("me mprimo")
    obj = get_object_or_404(Incidencias, slug=slug)
    return JsonResponse({
        "title": obj.title,
        "description": obj.description,
        "progreso": obj.progress,
        "prioridad": obj.priority,
        "due_date": obj.due_date,
        "type": obj.type
    })