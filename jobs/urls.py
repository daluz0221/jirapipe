from django.urls import path

from .views import HomeView

app_name = "jobs_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]