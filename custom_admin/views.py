from django.shortcuts import render

from django.views.generic import DetailView, CreateView
from django.views.generic.base import TemplateView

from moviesearch.models import Movie
from custom_admin.forms import MovieModelForm


class MainAdminView(TemplateView):
    template_name = ""


class MovieDetailView(DetailView):
    model = Movie
    template_name = ""
    context_object_name = "movie"  


class MovieCreateView(CreateView):
    model = Movie
    template_name = ""
    form_class = MovieModelForm