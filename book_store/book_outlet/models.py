from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Countries" #change plural display in admin dashboard
    
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries" #change plural display in admin dashboard

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def fullname(self):
        return self.first_name+" "+self.last_name
    
    def __str__(self):
        return self.fullname()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") # if already created a table, and then add this field,  
                                                               # this value can be null
                                                               #relate_name -> name for relation
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # db_index to best search performance
    # with blank=True, the field at the admin panel can be empty
    #with editable=False, the field doesn't appear at the admin panel
    published_countries = models.ManyToManyField(Country, null=False, related_name="books")
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
    def __str__(self): # how instances should be outputted
        return f"{self.title} ({self.rating})"
    
    