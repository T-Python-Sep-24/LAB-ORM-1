from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("new/", views.newPostView, name="newPostView"),
    path("postdetails/<int:postid>/", views.postDetailsView, name="postDetailsView"),
    path("update/<int:postid>/", views.updatePostView, name="updatePostView"),
    path("delete/<int:postid>/", views.deletePostView, name="deletePostView"),
    path("all/", views.allView, name="allView"),
    path("category/<category>/", views.categoryFilterView, name="categoryFilterView"),
]