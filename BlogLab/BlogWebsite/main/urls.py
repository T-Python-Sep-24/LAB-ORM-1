from . import views 
from django.urls import path

app_name = 'main'

urlpatterns = [ 

    path("",views.home_view,name="home_view"),
    path("addPost/",views.addPost_view, name="addPost_view"),
    path("DetailPage/<post_id>/",views.DetailPage_view , name="DetailPage_view"),
    path("update/<post_id>/",views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/" , views.post_delete_view , name="post_delete_view"),
]