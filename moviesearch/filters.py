import django_filters
from django import forms

from .models import Movie, Genre


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Название фильма")
    genre = django_filters.ModelChoiceFilter(
        queryset=Genre.objects.all(), 
        widget=forms.Select,
        empty_label="Выберите жанр"
    )

    class Meta:
        model = Movie
        fields = ("title", "genre", "age_restriction")