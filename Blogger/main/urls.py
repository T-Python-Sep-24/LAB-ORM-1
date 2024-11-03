from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('Post/',views.create_view,name="create_view"),
]