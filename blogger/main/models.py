from django.db import models
from django.utils import timezone

class Post(models.Model):


    class Category(models.TextChoices):
        TECHNOLOGY = 'Tech', 'Technology'
        LIFESTYLE = 'Life', 'Lifestyle'
        EDUCATION = 'Edu', 'Education'
        ENTERTAINMENT = 'Ent', 'Entertainment'


    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.TECHNOLOGY,
    )

    def __str__(self):
        return self.title