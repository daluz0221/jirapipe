from django.urls import path

from .views import LogoutView, UserManageView

app_name = "users_app"

urlpatterns = [
    path("login/", UserManageView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout")
]