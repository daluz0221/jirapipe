from django.urls import path

from .views import UserRegisterView, LoginView, LogoutView

app_name = "users_app"

urlpatterns = [
    path("login/", UserRegisterView.as_view(), name="user_register"),
    path("login/", LoginView.as_view(), name="user_login")
]