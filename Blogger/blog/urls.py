from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("post/", views.post_view, name="post_view"),
]