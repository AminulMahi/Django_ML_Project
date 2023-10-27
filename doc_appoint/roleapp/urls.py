from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.role_index, name='index'),
    path('/insert', views.insert, name='role_index'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update_index'),
    path('delete/<str:id>', views.delete, name='delete_item')
]