from django.contrib import admin
from django.utils.html import format_html
from .models import Genre, Movie, User, MonthlySubscription

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'age_restriction', 'preview')
    list_display_links = ['title',]
    search_fields = ('id', 'title', 'age_restriction', 'release_date', 'genre__name')
    list_filter = ('age_restriction', 'genre', 'release_date')
    list_editable = ['age_restriction',]
    ordering = ('release_date',)
    readonly_fields = ('join_date', 'update_date')
    fieldsets = (
        ('Основное', {
            'fields': ('picture', 'title', 'genre', 'rating', 'age_restriction')
        }),

        ('Дополнительно', {
            'fields': ('release_date', 'description'),
            'classes': ('collapse',)
        })
    )

    def preview(self, obj):
        if obj:
            return format_html('<img src="{}" width="100" height="80" />', format(obj.picture.url))
        return "Нет картинки"
    
    preview.short_description = "Превью"


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie_count')
    list_display_links = ('name',)
    search_fields = ('id', 'name')
    ordering = ('name',)
    fieldsets = (
        ('Жанр фильма', {
            'fields': ('name',)
        }),
    )

    def movie_count(self, obj):
        return obj.movie_set.count()
    movie_count.short_description = 'Количество фильмов'


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uname', 'uemail')
    list_display_links = ('uname',)
    search_fields = ['uname']
    ordering = ('id',)
    fieldsets = (
        ('Пользователь', {
            'fields': ('uname', 'uemail', 'upassword')
        }),
    )


class MonthlySubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__uname', 'balance')
    list_display_links = ('user__uname',)
    search_fields = ('user__uname',)
    ordering = ('id',)
    fieldsets = (
        ('Месячная подписка', {
            'fields': ('user', 'balance')
        }),
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MonthlySubscription, MonthlySubscriptionAdmin)