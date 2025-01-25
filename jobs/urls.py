from django.urls import path

from .views import ( 
    HomeView, 
    HistoryUserView, 
    TareasView, 
    CreateIncidenceView, 
    CreateIncidenceView, 
    CreateHistoryUserView, 
    CreateTareaView,
    UpdateIncidenceView,
    get_data
)

app_name = "jobs_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("history-user/<slug:incidencia_slug>/", HistoryUserView.as_view(), name="incidencia_detail"),
    path("tareas/<slug:incidencia_slug>/<slug:history_user_slug>/", TareasView.as_view(), name="history_user_detail"),

    path("incidencias/create-incidence/", CreateIncidenceView.as_view(), name="create_incidence"),
    path("incidencias/<slug:incidencia_slug>/create-history", CreateHistoryUserView.as_view(), name="create_huser"),
    path("tareas/<slug:incidencia_slug>/<slug:history_user_slug>/create-tare", CreateTareaView.as_view(), name="create_tarea"),

    path("incidencias/<slug:incidence_slug>/", UpdateIncidenceView.as_view(), name="update_incidence"),




    # Api
    path("api/incidence/<slug:slug>", get_data, name="get_data")


]