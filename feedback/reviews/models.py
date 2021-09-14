from django.db import models
from django.forms.fields import CharField

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField()