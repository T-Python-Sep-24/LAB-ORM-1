from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('add/', views.add_post_view, name='add_post'),
    path('', views.display_view, name='display'),
    path('details/<the_id>', views.details_view, name='details_view'),
    path('update/<the_id>', views.update_view, name='update_view'),
    path('delete/<the_id>', views.delete_view, name='delete_view'),
]
