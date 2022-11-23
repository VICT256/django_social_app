from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/like/', views.users_like, name='like'),
]