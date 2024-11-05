from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("mode/<mode>/", views.modeView, name="modeView"),
    path("postNotFound/", views.notFoundView, name="notFoundView"),
]