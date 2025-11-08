from django import forms
from .models import Movie

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'genre', 'age_restriction', 'rating']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма', 'rows': 5}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'age_restriction': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Возрастное ограничение'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рейтинг фильма', 'step': '0.1'}),
        }