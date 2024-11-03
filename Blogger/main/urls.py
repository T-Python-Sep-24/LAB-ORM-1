from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("new_post/", views.new_posts_view, name="new_posts_view"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)