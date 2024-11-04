from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        BUSINESS = 'BUS', 'Business'
        LIFESTYLE = 'LIFE', 'Lifestyle'
        EDUCATION = 'EDU', 'Education'
        HEALTH = 'HEALTH', 'Health'
        ENTERTAINMENT = 'ENT', 'Entertainment'

    title = models.CharField(max_length=1024)
    main_photo = models.ImageField(upload_to="blog_photos/", default="blog_photos/code.jpg")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TECHNOLOGY
    )

