from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('new/post', views.new_post_view, name='new_post_view'),
    path('detail/<blog_id>/', views.detail_view , name='detail_view'),
    path('update/<blog_id>/', views.update_view, name='update_view'),
    path('delete/<blog_id>/', views.delete_view, name='delete_view'),
    path('error/' , views.error_view , name="error_view"),
    
]