from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/',views.book_list, name = 'book_list'),
]
