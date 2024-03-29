from django.urls import path, re_path
from knox import views as knox_views

from users import api

app_name = "customers"

urlpatterns = [
    path("login/", api.LoginAPIView.as_view(), name="login"),
    re_path(r"logout/", knox_views.LogoutView.as_view(), name="logout"),
]
