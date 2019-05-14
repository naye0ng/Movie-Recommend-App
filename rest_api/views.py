from django.shortcuts import render, get_object_or_404
from movie.models import Genre, Movie, Review
from movie.serializers import MovieSerializer, ReviewSerailizer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# don2101
@api_view(['GET', 'POST'])
def movies(request):
    movie_list = Movie.objects.all()
    serializer = Response(movie_list, many=True)
    
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'message': '작성 완료'})
        return Response(serializer.error)
    else:
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        
        if serial.is_valid():
            serializer.save()
            
            return Response({'message': '수정 완료'})
        return Response(serializer.error)


@login_required
@api_view(['GET'])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.user in movie.user_like.all():
        movie.user_like.remove(request.user)
        
        return Response({'message': 'unlike'})
    else:
        movie.user_like.add(request.user)
        
        return Response({'message': 'like'})
    
    
def comments(request):
    pass

def comment_detail(request):
    pass


# naye0ng
def users(request) :
    pass

def user_detail(request) :
    pass
`
def user_follow(request) :
    pass

def login(request):
    pass

def logout(request):
    pass
