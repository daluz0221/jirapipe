from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.apps import apps
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView

from django.urls import reverse_lazy, reverse

from .forms import IncidenciaForm, HistoryUserForm, TareasForm
from .models import Incidencias, HistoriaUsuario, Tareas
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
        if not incidencias == "not found":
            ctx["user_histories"] = incidencias.get("history_list")
            ctx["parent_incidence"] = incidencias.get("incidencia_dict")
            ctx["history_user_form"] = HistoryUserForm
            ctx["history_user_update_form"] = HistoryUserForm
            
            return ctx
        
        self.template_name = "error.html"
        return ctx



class AllHistoryUserView(MyLoginRequiredView):
    template_name = "all_history_users.html"

    def get_context_data(self, **kwargs):
        ctx = super(AllHistoryUserView, self).get_context_data(**kwargs)

        ctx["histories_user"] = get_history_user("home")
            
        return ctx
       


class TareasView(MyLoginRequiredView):
    template_name = "jobs/tareas_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(TareasView, self).get_context_data(**kwargs)

        history_user_slug = self.kwargs.get("history_user_slug")
        incident = self.kwargs.get("incidencia_slug")
       
        incidencia = get_incidents("one", self.request.user, slug=incident)
        incidencias = get_tareas("all", history_user_slug=history_user_slug)
        if not (incidencia == "not found" or incidencias == "not found"):

            ctx["parent_history_user"] = incidencias.get("history_user_dict")
            ctx["parent_incidence"] = incidencia
            ctx["tareas"] = incidencias.get("tareas_list")
            ctx["tarea_form"] = TareasForm
            ctx["tarea_update_form"] = TareasForm
        
            return ctx
        
        self.template_name = "error.html"
        return ctx


class AllTareasView(MyLoginRequiredView):
    template_name = "all_tareas.html"

    def get_context_data(self, **kwargs):
        ctx = super(AllTareasView, self).get_context_data(**kwargs)

        ctx["tareas"] = get_tareas("home")
            
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
    context_object_name = 'data'

    def get_success_url(self):
        return self.request.path
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        incidence_slug = self.kwargs.get("incidencia_slug")
        incidence = get_incidents("one", self.request.user, slug=incidence_slug)
        ctx["incidencia"] = incidence

        return ctx


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





def get_incidence_data(request, slug):
    obj = get_object_or_404(Incidencias, slug=slug)
    return JsonResponse({
        "title": obj.title,
        "description": obj.description,
        "progreso": obj.progress,
        "prioridad": obj.priority,
        "due_date": obj.due_date,
        "type": obj.type
    })

class UpdateHistoryUserView(UpdateLoginRequired):
    model = HistoriaUsuario
    fields = (
        'title',
        'description',
        'estimate_time'
    )
    slug_url_kwarg = "huser_slug"
    template_name = "jobs/update_huser.html"
    success_url = "."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["incidencia_slug"] = self.kwargs.get("incidencia_slug")

        return ctx



def get_huser_data(request, slug):
    obj = get_object_or_404(HistoriaUsuario, slug=slug)
    return JsonResponse({
        "title": obj.title,
        "description": obj.description,
        "tiempo_estimado": obj.estimate_time
    })


class UpdateTareaView(UpdateLoginRequired):
    model = Tareas
    fields = (
        'title',
        'description',
        'state'
    )
    slug_url_kwarg = "job_slug"
    template_name = "jobs/update_job.html"
    success_url = "."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["incidencia_slug"] = self.kwargs.get("incidencia_slug")
        ctx["huser_slug"] = self.kwargs.get("huser_slug")

        return ctx


def get_job_data(request, slug):
    obj = get_object_or_404(Tareas, slug=slug)
    return JsonResponse({
        "title": obj.title,
        "description": obj.description,
        "state": obj.state
    })



def delete_object_from_model(request, model_name, object_slug):
    if request.method == "POST":
        model = apps.get_model("jobs", model_name)
        instance = get_object_or_404(model, slug=object_slug)
        instance.is_delete = True
        instance.save()

        messages.success(request, "Eliminación exitosa")
        return redirect(reverse("jobs_app:home"))
    
    return render(request, "error.html")