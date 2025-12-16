from django.urls import path, include


urlpatterns = [
    path('', include('api.yasg')),
    path('moviepoisk/', include('api.main.endpoints'))
]