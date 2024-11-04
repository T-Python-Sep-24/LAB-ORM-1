from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): 

    class Category(models.TextChoices):
        TECH = 'Tech', 'Technology'
        LIFESTYLE = 'Lifestyle', 'Lifestyle'
        TRAVEL = 'Travel', 'Travel'
        FOOD = 'Food', 'Food'

    title= models.CharField(max_length=2048)
    content= models.TextField()
    is_published= models.BooleanField(default=True)   
    published_at = models.DateTimeField(default=timezone.now)
    poster= models.ImageField(upload_to="images/", default="images/default.png")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.TECH)
  







    