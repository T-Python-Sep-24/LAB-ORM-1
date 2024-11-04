from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    class CategoryChoices(models.TextChoices):
        TECH = 'tech', 'Technology'
        LIFE = 'life', 'Lifestyle'
        EDU = 'edu', 'Education'
        NEWS = 'news', 'News'
        SPORTS = 'sports', 'Sports'
        
    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at  = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.png")
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.NEWS,
    )
