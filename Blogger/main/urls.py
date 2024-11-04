from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("blog/details/<blog_id>/", views.blog_view, name="blog_view"),
    # path("mode/dark/", views.dark_view, name="dark_view"),
    # path("mode/light/", views.light_view, name="light_view")
]