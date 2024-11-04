from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),  
    path('base/', views.base, name='base'),
    path('add/', views.add_post, name='add_post'),
    path('posts/', views.post_list, name='post_list'),
]
