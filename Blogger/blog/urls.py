from django.urls import path
from . import views


app_name='blog'

urlpatterns=[
    path('post/',views.new_post_view,name='new_post_view'),
    path('content/<blog_id>/',views.blog_content_view,name="blog_content_view"),
    path('update/<blog_id>/',views.blog_update_view,name="blog_update_view"),
    path('delete/<blog_id>/',views.blog_delete_view,name="blog_delete_view"),
    path('search/',views.search_blog_view,name='search_blog_view')
]