from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("create/", views.create_blog, name="create"),
    path("details/<blogID>/", views.blog_id,name="blog_id"),
    path("delete/<blogID>/", views.delete ,name="delete"),
    path("update/<blogID>/", views.update ,name="update"),

]