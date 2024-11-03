from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.add_post_view, name='home'),
    path('add/', views.add_post_view, name='add_post'),
    path('display/', views.display_view, name='display'),
]
