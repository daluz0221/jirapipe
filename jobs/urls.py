from django.urls import path

from .views import HomeView, HistoryUserView, TareasView, CreateIncidenceView, CreateIncidenceView, CreateHistoryUserView, CreateTareaView

app_name = "jobs_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("incidencias/create-incidence/", CreateIncidenceView.as_view(), name="create_incidence"),
    path("incidencias/<slug:incidencia_slug>/create-history", CreateHistoryUserView.as_view(), name="create_huser"),
    path("tareas/<slug:incidencia_slug>/<slug:history_user_slug>/create-tare", CreateTareaView.as_view(), name="create_tarea"),
    path("history-user/<slug:incidencia_slug>/", HistoryUserView.as_view(), name="incidencia_detail"),
    path("tareas/<slug:incidencia_slug>/<slug:history_user_slug>/", TareasView.as_view(), name="history_user_detail"),
]