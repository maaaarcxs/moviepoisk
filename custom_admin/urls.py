from django.urls import path
from .views import MovieDetailView, MovieCreateView, MainAdminView



urlpatterns = [
    path("custom-admin/", MainAdminView.as_view(), name="admin_view"),
    path('create-movie/', MovieCreateView.as_view(), name="create_movie"),
    path('movie/<slug:slug>', MovieDetailView.as_view(), name="movie_detail"),
]