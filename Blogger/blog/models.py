from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    class CategoryChoices(models.TextChoices):
       other='other', "other"
       Technology='tech' ,"Technology"
       lifestyle='lifestyle',"Lifestyle"
       Lifestyle="H&F" ,"Health & Fitness"
       eductation="E&C" ,"Education & Career"


    title=models.CharField(max_length=2048)
    content=models.TextField()
    is_published=models.BooleanField(default=True)
    published_at=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    category=models.CharField(max_length=56,choices=CategoryChoices.choices,default='other')