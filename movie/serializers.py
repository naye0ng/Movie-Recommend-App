from rest_framework import serializers
from .models import Movie, Review, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [ 'id','title', 'original_title', 'description', 'poster_url', 'trailer_url', 'genres', 'release_date', ]
        
class ReviewSerailizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = [ 'score', 'comment', 'id', 'user' ]
        read_only_fields = ['id', 'user']