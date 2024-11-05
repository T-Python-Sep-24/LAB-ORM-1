from django.db import models

class Blog(models.Model):
    class Category(models.TextChoices):
        NATURE = 'NAT', 'Nature'       
        PHYSICS = 'PHY', 'Physics'      
        CHEMISTRY = 'CHE', 'Chemistry' 
        PLANTS = 'PLA', 'Plants'        
        MATH = 'MTH', 'Mathematics'     
        SCIENCE = 'SCI', 'Science'    
    
    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", default="images/default.JPG")
    category = models.CharField(max_length=4, choices=Category.choices)

