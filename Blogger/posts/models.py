from django.db import models
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=2048,default="Default title here")
    content =models.TextField(default="Default content here")
    is_published =models.BooleanField(default=True)
    published_at =models.DateTimeField(default=now)
    