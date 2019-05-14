from django.urls import path
from . import views

app_name='administor'

urlpatterns = [
    path('users/',views.users, name='users'),
    path('movies/',views.movies, name='movies'),
]
