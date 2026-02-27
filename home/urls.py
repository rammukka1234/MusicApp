from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('telugu/', views.telugu, name='telugu'),
    path('hindi/', views.hindi, name='hindi'),
    path('english/', views.english, name='english'),
    path('about/', views.about, name='about'),
]