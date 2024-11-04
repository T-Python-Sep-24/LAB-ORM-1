from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="posts"

urlpatterns = [
    
    path('create/', views.create_post_view, name='create_post_view'),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
    
] 
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Custom error handlers
handler404 = 'posts.views.custom_404_view'
