from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("create/", views.create_blog_view, name="create_blog_view"),
    path("details/<blog_id>/", views.blog_view, name="blog_view"),
]

