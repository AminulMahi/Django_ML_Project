from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/blog', views.blog, name='blog_index'),
    path('upload/', views.upload, name = 'upload')
]