from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import BooleanField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100) # if already created a table, and then add this field,  
                                                        # this value can be null
    is_bestselling = models.BooleanField(default=False)
    
def __str__(self): # how instances should be outputted
    return f"{self.title} ({self.rating})"
