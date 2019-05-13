from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    # followers : 자신이 follow 하는 User
    # followings : 자신을 follow 하고 있는 User
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')