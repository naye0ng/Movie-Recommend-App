from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('users/',views.users,name='users'),
    path('movies/',views.movies,name='movies'),
    # TODO : (Vue.js로 CRUD)movie app, user app의 rest api로 넘김 or admin app 자체적으로 처리
]