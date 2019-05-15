from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.movies), # GET, POST
    path('movies/<int:movie_id>/',views.movie_detail), # GET, PUT, DELETE
    path('movies/<int:movie_id>/like/',views.movie_like), # GET
    path('movies/<int:movie_id>/reviews/',views.reviews), # GET, POST
    path('movies/<int:movie_id>/reviews/<int:review_id>/',views.review_detail), # PUT, DELETE
    path('get_genre/', views.get_genre),
    path('get_movie/', views.get_movie),
    
    path('genres/', views.genres), # GET
    path('users/', views.users), # GET
    path('users/<int:user_id>/', views.user), # GET, PUT, DELETE
    path('users/<int:user_id>/follow/', views.user_follow), # GET
]