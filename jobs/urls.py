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
    UpdateHistoryUserView,
    UpdateTareaView,
    get_incidence_data,
    get_huser_data,
    get_job_data,
    delete_object_from_model
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
    path("history-user/<slug:incidencia_slug>/<slug:huser_slug>/", UpdateHistoryUserView.as_view(), name="update_history"),
    path("job/<slug:incidencia_slug>/<slug:huser_slug>/<slug:job_slug>/", UpdateTareaView.as_view(), name="update_history"),

    path("delete/<str:model_name>/<slug:object_slug>/", delete_object_from_model, name="delete-object"),




    # Api
    path("api/incidence/<slug:slug>", get_incidence_data, name="get_incidence_data"),
    path("api/history/<slug:slug>", get_huser_data, name="get_history_data"),
    path("api/job/<slug:slug>", get_job_data, name="get_job_data"),


]