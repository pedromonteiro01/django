from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
    #imagefield don't need to validate the file type