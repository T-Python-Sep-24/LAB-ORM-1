from django.urls import path
from . import views
app_name = 'bloggerApp'

urlpatterns = [
    path('', views.main_view, name="main_view"),
    # path('post/create/', views.create_post_view, name="create_post_view"),
]
