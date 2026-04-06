from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name = "login"),
    path('', include([path('logins/',views.login)])),
    path('registration/', views.registration, name = "registration"),
    path('', include([path('registration/', views.registration)])),

]