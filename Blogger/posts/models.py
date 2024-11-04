from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=2048,default="Default title here")
    content =models.TextField(default="Default content here")
    is_published =models.BooleanField(default=True)
    published_at =models.DateTimeField(default=now)
    poster = models.ImageField(upload_to="images/",default='images/default.jpg',blank=False)

    class Category(models.TextChoices):
        MINDFULNESS = "Mindfulness and Meditation"
        MENTAL_HEALTH = "Mental Health"
        PHYSICAL_WELLNESS = "Physical Wellness"
        SELF_CARE_RITUALS = "Self-Care Rituals"
        PERSONAL_GROWTH = "Personal Growth"

    category = models.CharField(max_length=50,choices=Category,default=Category.SELF_CARE_RITUALS)
