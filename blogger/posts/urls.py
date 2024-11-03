from django.urls import path
from .views import home, add_post, edit_post, delete_post, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_post, name='add_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('about/', about, name='about'),  # Add this line
    path('contact/', contact, name='contact'),  # Add this line
]
