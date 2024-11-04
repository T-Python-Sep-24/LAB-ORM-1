from django.urls import path
from . import views
app_name = 'postsApp'

urlpatterns = [
    path('create/', views.create_post_view, name='create_post_view'),


]