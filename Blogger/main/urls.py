from . import views
from django.urls import path


app_name="main"
urlpatterns=[

    path("",views.home_view,name="home_view"),
    path("post/",views.new_post,name="new_post"),
    path("detail/<post_id>/",views.post_detail,name="post_detail"),
    path("update/<post_id>/",views.post_update,name="post_update"),
    path("delete/<post_id>/",views.post_delete,name="post_delete"),
]