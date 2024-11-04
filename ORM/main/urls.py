from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.view_home, name="home"),
    path("create/", views.create_blog, name="create"),
]
