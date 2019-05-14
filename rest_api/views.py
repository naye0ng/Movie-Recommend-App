from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from movie.models import Genre, Movie, Review
from movie.serializers import MovieSerializer, ReviewSerailizer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
import http.client
import json

TMBb_KEY = "c32b7a92dabcaf36aea7c9e6d9ad689e"

# Create your views here.

# don2101
@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        movie_list = Movie.objects.all()
        serializer = MovieSerializer(movie_list, many=True)
        
        return Response(serializer.data)
    # TODO: 관리자 확인
    else:
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(genre)
            
            return Response({'message': '작성 완료'})
        return Response(serializer.error)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'message': '수정 완료'})
        return Response(serializer.error)
    else:
        movie.delete()


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
    

@api_view(['GET', 'POST'])
def reviews(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'GET':
        review_list = movie.review_set.all()
        
        serializer = ReviewSerailizer(review_list, many=True)
        
        return Response(data=serializer.data)
    else:
        serializer = ReviewSerailizer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(movie=movie, user=request.user)

            return Response({'message': '작성 완료'})
        return Response(serializer.error)


@login_required
@api_view(['PUT', 'DELETE'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'PUT':
        serializer = ReviewSerailizer(review, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'message', '수정 완료'})
        return Response(serializer.error)
    else:
        review.delete()


def get_genre(request):
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMBb_KEY}&language=ko-KR"
    
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    
    payload = "{}"
    
    conn.request("GET", genre_url, payload)
    
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    dic = json.loads(data)
    genre_list = dic.get('genres')
    
    for genre in genre_list:
        Genre.objects.create(code=genre.get('id'), name=genre.get('name'))
    
def get_movie(request):
    movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMBb_KEY}&language=ko-KR&page=1"

    conn = http.client.HTTPSConnection("api.themoviedb.org")
    
    payload = "{}"
    
    conn.request("GET", movie_url, payload)
    
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    dic = json.loads(data)
    
    print(dic)


# naye0ng
def users(request) :
    pass

def user_detail(request) :
    pass

def user_follow(request) :
    pass

def login(request):
    pass

def logout(request):
    pass
