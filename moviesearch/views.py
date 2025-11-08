from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.decorators import login_required


from .models import Movie, Genre
from django.urls import reverse_lazy
from .forms import MovieModelForm
from .filters import MovieFilter



class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'
    paginate_by = 10
    extra_context = {
        'title': 'Главная страница',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        genre_slug = self.request.GET.get('genre') 
        year = self.request.GET.get('year')
        theme = self.request.GET.get('theme')

        if q:
            queryset = queryset.filter(title__icontains=q)
        if genre_slug:
            queryset = queryset.filter(genre__slug=genre_slug)
        if year:
            queryset = queryset.filter(release_date__year=year)
        if theme:
            queryset = queryset.filter(description__icontains=theme)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


def moviefilterr(request):
    movies = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movies)
    return render(request, "home.html", {'filter': movie_filter})


class MoviesByGenreListView(ListView):
    model = Movie
    template_name = 'moviesearch/home.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        genre_slug = self.kwargs['genre_slug']
        return Movie.objects.filter(genre__slug=genre_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.get(slug=self.kwargs['genre_slug'])
        context['title'] = f'Жанр: {genre.name}'
        context['genre'] = genre
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'moviesearch/movie_detail.html'
    context_object_name = 'movie'
    paginate_by = 10
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieModelForm
    template_name = 'moviesearch/add_movie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление фильма'
        return context
    
    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'slug': self.object.slug})