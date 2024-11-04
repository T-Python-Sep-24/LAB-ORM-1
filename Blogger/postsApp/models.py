from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField("photographyCategory", "portrait nature architecture animals plants objects")
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    published_by = models.CharField(max_length=1024)
    post_img = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.TextChoices()