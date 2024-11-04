from django.urls import path
from . import views
app_name = 'postsApp'

urlpatterns = [
    path('create/', views.create_post_view, name='create_post_view'),
    path('details/<post_id>/', views.post_details_view, name='post_details_view'),
    path('update/<post_id>/', views.update_post_view, name="update_post_view"),
    path('delete/<post_id>/', views.delete_post_view, name="delete_post_view"),
]