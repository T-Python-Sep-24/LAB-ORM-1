from django.db import models

# Create your models here.

class Game(models.Model):

    title = models.CharField(max_length=1024)
    description = models.TextField()
    publisher = models.CharField(max_length=256)
    rating = models.SmallIntegerField()
    release_date = models.DateField()




