from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("new_post/", views.new_posts_view, name="new_posts_view"),


]