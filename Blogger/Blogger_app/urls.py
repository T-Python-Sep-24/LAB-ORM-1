from django.urls import path
from . import views


app_name = "Blogger_app"

urlpatterns = [
path("", views.homepage, name="homepage"),
path("new/", views.newPost, name="newPost"),

]


