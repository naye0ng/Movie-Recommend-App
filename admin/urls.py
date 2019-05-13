from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('users/',views.users,name='users'),
    path('movies/',views.movies,name='movies'),
    # TODO : vue로 CRUD 처리 : Rest API 추가
    # path('api/user/<int_userId>/', views.user, name='user'),
]