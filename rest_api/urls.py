from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.movies)
]