from django.db import models

# Create your models here.

class Post(models.Model):

    CATEGORY_CHOICES = [
        ('portrait', 'portrait'),
        ('nature', 'nature'),
        ('architecture', 'architecture'),
        ('animals', 'animals'),
        ('plants', 'plants'),
        ('objects', 'objects'),
        ('other', 'other'),
    ]

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    published_by = models.CharField(default="Anonymous", max_length=1024)
    post_img = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")