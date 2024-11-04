from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=1024)
    main_photo = models.ImageField(upload_to="blog_photos/", default="blog_photos/code.jpg")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    Published_at = models.DateTimeField(auto_now=True)

