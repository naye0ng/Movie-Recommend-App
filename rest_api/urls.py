from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies), # GET, POST
    path('movies/<int:movie_id>/',views.movie_detail), # GET, PUT, DELETE
    path('movies/<int:movie_id>/like/',views.movie_like), # GET
    path('movies/<int:movie_id>/comments/',views.comments), # GET, POST
    path('movies/<int:movie_id>/comments/<int:comment_id>/',views.comment_detail), # PUT, DELETE
    path('users/', views.users), # GET
    path('users/<int:user_id>/', views.user_detail), # GET, PUT, DELETE
    path('users/<int:user_id>/follow/', views.user_follow), # GET
    path('accounts/login/', views.login), # POST
    path('accounts/logout/', views.logout), # POST
]