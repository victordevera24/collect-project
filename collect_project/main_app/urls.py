from os import abort
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    
    # http://localhost:8000/about/
    path('about/', views.about, name='about'),

    # http://localhost:8000/fish/
    path('fish/', views.fish_index, name='index')
]