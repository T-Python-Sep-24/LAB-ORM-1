from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content  = models.TextField()
    isPublished = models.BooleanField(default=True)
    publishedAt = models.DateField(auto_now=True)