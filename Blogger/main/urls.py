from django.urls import path
from .views import homepage, add_post , post_detail, update_post, delete_post

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add_post, name='add_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', update_post, name='update_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
]
