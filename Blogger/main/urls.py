from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name = "home_view"),
    path("add/", views.add_view, name = "add_view"),
    path("details/<post_id>/", views.post_details_view, name = "post_details_view"),
    path("notfound/", views.not_found_view, name = "not_found_view"),
    path("update/<post_id>/", views.update_view, name = "update_view"),
    path("delete/<post_id>/", views.delete_view, name = "delete_view" ),
]