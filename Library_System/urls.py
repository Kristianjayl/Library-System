from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/',views.book_list, name = 'book_list'),
    path('about_us/', views.about, name = 'about_us'),
    path('help/',views.help, name = 'help'),
    path('FAQ/',views.FAQ, name = 'FAQ'),
    path('TaP/',views.TaP, name = 'TaP'),
    path('contact/',views.contact, name = 'contact'),
]
