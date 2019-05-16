from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from movie.models import Genre
from .forms import CustomUserCreationForm

# Create your views here.
def login(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)

        if form.is_valid() :
            # 로그인하여 원래 주소로 넘겨주기
            auth_login(request, form.get_user())
            # 이부분 추가
            return redirect(request.GET.get('next') or 'home')

    form = AuthenticationForm()
    content = {
        'form' :form,
    }
    return render(request,'accounts/login.html',content)

def logout(request) :
    auth_logout(request)

    return redirect('home')



def signup(request) :
    if request.method =='POST' :
        user_form = CustomUserCreationForm(request.POST)
        
        if user_form.is_valid()  :
            user = user_form.save()

            # 로그인 처리 넣기
            return redirect('accounts:login')

    form = CustomUserCreationForm()
    content = {
        'form' : form
    }
    return render(request,'accounts/signup.html',content)


def detail(request, username):
    user = User.objects.get(username=username)
    follower_count = user.followings.count()
    like_genres = user.like_genre.all()
    genre_list = Genre.objects.all()
    
    content = {
        'user': user,
        'follower_count': follower_count,
        'genre_list': genre_list,
        'like_genres': like_genres,
    }
    
    return render(request, 'accounts/detail.html', content)
    
    