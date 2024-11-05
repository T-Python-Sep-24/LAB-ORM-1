from django.db import models

# Create your models here.

class Post(models.Model):
    class CATEGORY_CHOICES(models.TextChoices):

        portrait = 'portrait', 'Portrait'
        nature = 'nature', 'Nature'
        architecture = 'architecture', 'Architecture'
        animals = 'animals', 'Animals'
        plants = 'plants', 'Plants'
        objects = 'objects', 'Objects'



    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    published_by = models.CharField(default="Anonymous", max_length=1024)
    post_img = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES.choices, default="other")