from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    
    path('create/', views.create_post_view, name='create_post_view'),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    
]
