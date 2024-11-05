from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True) 

    class Category(models.TextChoices):
        TECH = 'Tech', 'Technology'
        LIFE = 'Life', 'Lifestyle'
        FOOD = 'Food', 'Food'
        TRAVEL = 'Travel', 'Travel'
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.TECH)

    def __str__(self):
        return self.title
