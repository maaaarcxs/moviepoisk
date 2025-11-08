from django.urls import path
from .views import MovieListView, MoviesByGenreListView


urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('genre/<slug:genre_slug>/', MoviesByGenreListView.as_view(), name='movies_by_genre'),
]