from os import abort
from django.urls import path, include
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    # http://localhost:8000/about/
    path('about/', views.about, name='about'),
    # http://localhost:8000/fish/
    path('fish/', views.fish_index, name='index'),
    path('fish/<int:fish_id>', views.fish_detail, name='detail'),
    path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
    path('fish/<int:pk>/update', views.FishUpdate.as_view(), name='fish_update'),
    path('fish/<int:pk>/delete', views.FishDelete.as_view(), name='fish_delete'),
    path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('fish/<int:fish_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('fish/<int:fish_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]