from rest_framework import serializers
from .models import Movie, Review, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [ 'title', 'description', 'poster_url', 'trailer_url', 'audience', 'genre', ]
        
        
class ReviewSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [ 'score', 'comment', ]