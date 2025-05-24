from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('Portfolio_Dj/', book_list, name='book_list'),
    path('add/',book_create, name='book_create'),
    path('edit/<int:pk>/', book_update, name='book_update'),
    path('delete/<int:pk>/',book_delete, name='book_delete'),
]
