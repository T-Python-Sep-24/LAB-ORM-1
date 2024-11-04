from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=now)

    