from . import views
from django.urls import path

app_name="posts"

urlpatterns=[
    path('add/',views.add_post_view,name="add_post_view")
]