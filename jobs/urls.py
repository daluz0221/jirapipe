from django.urls import path

from .views import HomeView, HistoryUserView

app_name = "jobs_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("incidencias/<slug:incidencia_slug>/", HistoryUserView.as_view(), name="incidencia_detail")
]