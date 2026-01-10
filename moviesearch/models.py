from django.db import models

from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр фильма', max_length=100)
    slug = models.SlugField(verbose_name="URL жанра")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    picture = models.ImageField(upload_to='movies/', verbose_name='Превью', null=True, blank=True)
    title = models.CharField(verbose_name='Название фильма', max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name='Описание фильма', max_length=1300)
    release_date = models.DateField(verbose_name='Дата выпуска')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр фильма')
    age_restriction = models.CharField(verbose_name='Возрастное ограничение', max_length=10)
    rating = models.FloatField(verbose_name='Рейтинг фильма', default=0.0)
    join_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):         
        return f'{self.id}  {self.title} ({self.age_restriction})'
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


# class User(models.Model):
#     uname = models.CharField(verbose_name='Имя пользователя', max_length=150)
#     uemail = models.EmailField(verbose_name='Электронная почта', unique=True)
#     upassword = models.CharField(verbose_name='Пароль', max_length=128)

#     def __str__(self):
#         return f'{self.uname} ({self.uemail})'
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'


# class MonthlySubscription(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
#     balance = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Баланс',)

#     def __str__(self):
#         return f'Contract for {self.user.uname}, balance: {self.balance}'
    
#     class Meta:
#         verbose_name = "Подписчик"
#         verbose_name_plural = 'Подписчики'