from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    category_options = [('tech', 'Tech'),('games', 'Games'),('advice', 'Advice'),('business', 'Business')]
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)  
    image = models.ImageField(upload_to="images/",default="images/default.jpg")
    category = models.CharField(max_length=50, choices=category_options)

