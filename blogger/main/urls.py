from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('post/', views.add_post, name='add_post'),
    path('details/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('update/<int:blog_id>/', views.update_post, name='update_post'),
    path('delete/<int:blog_id>/', views.delete_post, name='delete_post'),
]

handler404 = 'main.views.custom_view'