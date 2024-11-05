from django.db import models

class Post(models.Model):
    class Categories(models.TextChoices):
        General = "General", "General"
        Travel = "Travel", "Travel"
        Sport = "Sport", "Sport"
        Entertainment = "Entertainment", "Entertainment"
        Technology = "Technology", "Technology"
        Business=  "Business", "Business"
        Culture = "Culture", "Culture"

    title = models.CharField(max_length=512)
    content  = models.TextField()
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    category = models.CharField(max_length=64, choices=Categories.choices)
    isPublished = models.BooleanField(default=True)
    publishedAt = models.DateTimeField(auto_now=True )