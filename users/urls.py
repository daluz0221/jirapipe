from django.urls import path

from .views import UserRegisterView, LoginView, LogoutView

app_name = "users_app"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_register"),
    path("login/", LoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout")
]