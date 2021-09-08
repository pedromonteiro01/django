from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    
def __str__(self): # how instances should be outputted
    return f"{self.title} ({self.rating})"
