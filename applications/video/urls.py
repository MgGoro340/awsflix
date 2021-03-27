from django.contrib import admin
from django.urls import path, re_path, include

from . import views 

urlpatterns = [
    path('api/videos/list', views.VideoListApiView.as_view()),
]
