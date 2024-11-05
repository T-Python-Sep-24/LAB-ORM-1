from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("new_post/", views.new_posts_view, name="new_posts_view"),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
    path("published/", views.post_published_view, name="post_published_view"),
    path("updated_success//<post_id>/", views.post_success_updated_view, name="post_success_updated_view"),
    path("all/", views.post_all_view, name="post_all_view"),
    path("search/", views.search_post_view, name="search_post_view"),
]
