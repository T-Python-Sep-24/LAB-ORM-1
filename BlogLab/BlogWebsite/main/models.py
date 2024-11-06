from django.db import models

# Create your models here.

class Post(models.Model):
    class Category(models.TextChoices):
        TECHNOLOGY = 'Tech', 'Technology'
        LIFESTYLE = 'Life', 'Lifestyle'
        EDUCATION = 'Edu', 'Education'
        HEALTH = 'Hlth', 'Health'
        BUSINESS = 'Biz', 'Business'
        ENTERTAINMENT = 'Ent', 'Entertainment'
        
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default='images/ai-education.webp') 
    category = models.CharField(max_length=64, choices=Category.choices, default=Category.TECHNOLOGY)

    def __str__(self):
        return self.title