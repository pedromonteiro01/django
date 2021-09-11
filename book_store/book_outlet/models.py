from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # if already created a table, and then add this field,  
                                                               # this value can be null
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # db_index to best search performance
    # with blank=True, the field at the admin panel can be empty
    #with editable=False, the field doesn't appear at the admin panel
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
    def __str__(self): # how instances should be outputted
        return f"{self.title} ({self.rating})"
    
    