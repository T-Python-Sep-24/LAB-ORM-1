from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    #  inner class uses Django TextChoices to define the choices for category
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        HEALTH = 'HEALTH', 'Health'
        LIFESTYLE = 'LIFESTYLE', 'Lifestyle'
        SPORTS = 'SPORTS', 'Sports'
        EDUCATION = 'EDUCATION', 'Education'

    title = models.CharField(max_length = 256)
    content = models.TextField()
    is_published = models.BooleanField(default = True)
    published_at = models.DateTimeField(default = datetime.now())
    image = models.ImageField(upload_to = "main/images", default = "images/default.jpg")
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.TECHNOLOGY,)
