from django.db import models
from datetime import date
# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField() 
    published_at = models.DateField(auto_now_add=True)  
    poster = models.ImageField(upload_to="images/" , default="images/default.jpg")
    # kind=models.CharField(max_length=1000 , default="Other")

    categoryChoices= models.TextChoices("Category", "technology business sport")
    category  = models.CharField(max_length=64, choices=categoryChoices.choices, default=categoryChoices.business)
