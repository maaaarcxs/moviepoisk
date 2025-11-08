from django.urls import path
from .views import login_custom, register_view


urlpatterns = [
    path("login/", login_custom, name="login"),
    path("register/", register_view, name="register")
]