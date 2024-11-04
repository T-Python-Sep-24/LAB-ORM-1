from django.urls import path
from . import views
from django.conf.urls import handler404
from .views import custom_404_view


app_name = "Blogger_app"

urlpatterns = [
path("", views.homepage, name="homepage"),
path("new/", views.newPost, name="newPost"),
path("deatail/<blog_id>", views.blogDeatails, name="blogDeatails"),
path("update/<blog_id>", views.blogUpdate, name="blogUpdate"),
path("delete/<blog_id>", views.blogDelete, name="blogDelete"),

]

handler404 = custom_404_view