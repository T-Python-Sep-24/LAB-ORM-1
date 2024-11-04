from django.db import models

class Post(models.Model):

    CATEGORIES = {
        "General": "General",
        "Travel": "Travel",
        "Sport": "Sport",
        "Entertainment": "Entertainment",
        "Technology": "Technology",
        "Business": "Business",
        "Culture": "Culture"
    }

    title = models.CharField(max_length=2048)
    content  = models.TextField()
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    category = models.CharField(max_length=256, choices=CATEGORIES)
    isPublished = models.BooleanField(default=True)
    publishedAt = models.DateField(auto_now=True)