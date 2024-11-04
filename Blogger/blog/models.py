from django.db import models
from django.utils.timezone import now
from datetime import datetime

class Blog(models.Model):
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=datetime.now)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")

    