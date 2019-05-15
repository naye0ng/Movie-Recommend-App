from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"장르: {self.name}"


class Movie(models.Model):
    movie_code = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    description = models.TextField()
    poster_url = models.CharField(max_length=200)
    trailer_url = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movie')
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie', blank=True)

    def __str__(self):
        return f"영화 제목: {self.title}"


class Review(models.Model):
    score = models.IntegerField()
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"댓글: {self.comment}"

