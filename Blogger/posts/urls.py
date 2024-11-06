from . import views
from django.urls import path

app_name="posts"

urlpatterns=[
    path('add/',views.add_post_view,name="add_post_view"),
    path('details/<post_id>/', views.post_detail_view, name="post_detail_view"),
    path('update/<post_id>/', views.post_update_view, name="post_update_view"),
    path('delete/<post_id>/', views.post_delete_view, name="post_delete_view"),
    path('notfound/',views.notfound_view,name="notfound_view"),
    path('all/',views.all_posts_view,name="all_posts_view"),
    path('search/',views.search_posts_view,name="search_posts_view"),

]