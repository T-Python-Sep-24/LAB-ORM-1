from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class Category(models.TextChoices):
        PHILOSOPHY = 'Philosophy', 'Philosophy'
        MEDICINE = 'Medicine', 'Medicine'
        SCIENCE = 'Science', 'Scientists'
        FICTIONAL = 'Fictional', 'Fictional Characters'

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to="images/",default="images/default.jpf")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.SCIENCE)

