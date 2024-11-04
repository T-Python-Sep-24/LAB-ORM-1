from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('Post/',views.create_view,name="create_view"),
    path('detail/<post_id>/',views.detail_view,name="detail_view"),
    path('update/<post_id>/',views.update_view,name="update_view"),
    path('delete/<post_id>/',views.delete_view,name="delete_view"),
]