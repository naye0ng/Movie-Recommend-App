from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_url = models.CharField(max_length=200)
    trailer_url = models.CharField(max_length=200)
    audience = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Review(models.Model):
    score = models.IntegerField()
    comment = models.CharField(max_length=300)