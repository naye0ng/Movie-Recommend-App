from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from movie.models import Genre


# Create your models here.
class User(AbstractUser) :
    isAdmin = models.BooleanField(default=False)
    # followers : 자신이 follow 하는 User
    # followings : 자신을 follow 하고 있는 User
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    # like_genre : user가 좋아하는 genre
    # liked_by : genre를 좋아하는 user
    like_genre = models.ManyToManyField(Genre, related_name='liked_by', blank=True)