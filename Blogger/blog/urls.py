from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("create/", views.create_blog_view, name="create_blog_view"),
    path("details/<blog_id>/", views.blog_view, name="blog_view"),
    path("update/<blog_id>/", views.update_blog_view, name="update_blog_view"),
    path("delete/<blog_id>/", views.delete_blog_view, name="delete_blog_view")
]



