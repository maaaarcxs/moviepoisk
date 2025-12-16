from django.urls import path
from .api import custom_login, custom_register, custom_logout, profile
url_patterns = [
    path('login/', custom_login, name="custom_login"),
    path('register/', custom_register, name="custom_register"),
    path('logout/', custom_logout, name="custom_logout"),
    path('profile/', profile, name="profile")
]
