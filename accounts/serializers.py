from rest_framework import serializers
from .models import User
from movie.serializers import GenreSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    like_genre = GenreSerializer(many=True, read_only=True)
    
    class Meta :
        model = User
        fields = ['id', 'username', 'isAdmin', 'like_genre',]