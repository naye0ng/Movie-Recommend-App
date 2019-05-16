from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from movie.models import Genre, Movie, Review
from accounts.models import User
from movie.serializers import MovieSerializer, ReviewSerailizer, GenreSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
import http.client
import json

from accounts.serializers import CustomUserSerializer
from accounts.models import User

TMBb_KEY = "c32b7a92dabcaf36aea7c9e6d9ad689e"

# Create your views here.

# don2101

def main(request):
    return render(request, 'rest_api/main.html')
    
def administor(request):
    return render(request, 'rest_api/admin.html')

@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        movie_list = Movie.objects.order_by('-release_date').all()
        serializer = MovieSerializer(movie_list, many=True)
        
        return Response(serializer.data)
    # TODO: 관리자 확인
    elif request.method == 'POST':
        # 영화 정보 생성  
        genres = Genre.objects.filter(id__in= request.data['genres'])

        movie = Movie()
        movie.original_title = request.data['original_title']
        movie.title =request.data['title']
        movie.description =request.data['description']
        movie.poster_url =request.data['poster_url']
        movie.release_date =request.data['release_date']
        movie.trailer_url =request.data['trailer_url']
        movie.save()
        
        for genre in genres :
            movie.genres.add(genre)
        
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    print('ddddddd')
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
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
    
@login_required
@api_view(['POST', 'GET'])
def reviews(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        review_list = movie.review_set.all()
        
        serializer = ReviewSerailizer(review_list, many=True)
        
        return Response(data=serializer.data)
    else:
        serializer = ReviewSerailizer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print(serializer)
            serializer.save(movie=movie, user=request.user)

            return Response(serializer.data)
        return Response(serializer.error)


@login_required
@api_view(['PUT', 'DELETE'])
def review_detail(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'PUT':
        serializer = ReviewSerailizer(review, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'message', '수정 완료'})
        return Response(serializer.error)
    else:
        review.delete()
        
        return Response({'id': review_id})


@api_view(['GET'])
def movie_recommend(request, user_id):
    pass




# naye0ng
@api_view(['GET'])
def genres(request) :
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@login_required
@api_view(['GET'])
def users(request) :
    users = User.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET','PUT', 'DELETE'])
def user(request, user_id) :
    user = get_object_or_404(User,pk=user_id)
    print("요청 들어옴")
    # 해당하는 user 1명의 정보 반환, 개인페이지에서 사용가능
    if request.method == 'GET' :
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
        
    elif request.method == 'PUT' :
        # 유저 정보 변경
        user.username = request.data['username']
        user.isAdmin = request.data['isAdmin']
        user.save()
        serializer = CustomUserSerializer(user,many=False)
        return Response(serializer.data)
        
    elif request.method == 'DELETE' :
        # 유저 정보 삭제
        serializer = CustomUserSerializer(user,many=False)
        user.delete()
        return Response(serializer.data)


@api_view(['GET'])
def user_follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    # if request.user != user:
    if user in request.user.followers.all():
        request.user.followers.remove(user)
        
        return Response({'message': 'follow 취소'})
    else:
        request.user.followers.add(user)
        
        return Response({'message': 'follow 추가'})
        

@api_view(['GET'])
def check_follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if user in request.user.followers.all():
        
        return Response({'message': True})
    else:
        request.user.followers.add(user)
        
        return Response({'message': False})
        
    
    








# 장르, 영화 정보 수집, model로 옮기기?
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
    for i in range(1, 11):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMBb_KEY}&language=ko-KR&page={i}"
        print(movie_url)
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        payload = "{}"
        conn.request("GET", movie_url, payload)
        
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        movie_list = json.loads(data).get('results')
        
        for movie in movie_list:
            genre_list = movie.get('genre_ids')
            created_movie=Movie.objects.create(
                movie_code=movie.get('id'),
                title=movie.get('title'),
                original_title=movie.get('original_title'),
                poster_url="https://image.tmdb.org/t/p/original"+movie.get('poster_path'),
                description=movie.get('overview'),
                release_date=movie.get('release_date'),
            )
            
            for genre in genre_list:
                created_movie.genres.add(Genre.objects.get(code=genre))
