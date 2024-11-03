from django.urls import path
from .views import homepage, add_post

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add_post, name='add_post'),
]