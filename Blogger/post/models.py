from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content  = models.TextField()
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    isPublished = models.BooleanField(default=True)
    publishedAt = models.DateField(auto_now=True)