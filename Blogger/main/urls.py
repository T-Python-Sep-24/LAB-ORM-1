from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path("",views.home_page_view,name="home_page_view"),
]