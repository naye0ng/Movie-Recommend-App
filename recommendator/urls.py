"""recommendator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from movie import urls
# from administor import urls
# from accounts import urls
from rest_api import urls
import rest_api
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rest_api.views.main, name="home"),
    path('movie/', include('movie.urls')),
    path('accounts/',include('accounts.urls')),
    path('administor/', include('administor.urls')),
    path('api/v1/', include('rest_api.urls')),
    path('docs/', get_swagger_view(title="Movie Recommend App : API Document")),
]

