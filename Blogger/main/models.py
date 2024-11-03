from django.db import models
from django.utils import timezone

# Create your models here.
class Blogger(models.Model):
   
   titel=models.CharField(max_length=2048)
   contant=models.TextField()
   is_published=models.BooleanField(default= True)
   published_at=models.DateTimeField(timezone.now)
   



