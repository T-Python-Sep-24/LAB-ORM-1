from django.db import models
from django.utils.timezone import now
from datetime import datetime

class Blog(models.Model):
    class Category(models.TextChoices):
        TECHNOLOGY = 'Tech', 'Technology'
        LIFESTYLE = 'Life', 'Lifestyle'
        TRAVEL = 'Travel', 'Travel'
        FOOD = 'Food', 'Food'
        EDUCATION = 'Edu', 'Education'
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=datetime.now)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.TECHNOLOGY,
    )
    