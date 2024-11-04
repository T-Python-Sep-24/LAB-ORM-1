from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    class Category(models.TextChoices):
        TECH = 'TE', 'Technology'
        LIFESTYLE = 'LI', 'Lifestyle'
        TRAVEL = 'TR', 'Travel'
        FOOD = 'FO', 'Food'

    title = models.CharField(max_length=2048)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=2, choices=Category.choices, default=Category.TECH)

    def __str__(self):
        return self.title

