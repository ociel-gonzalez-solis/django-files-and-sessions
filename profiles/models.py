from django.db import models

# Create your models here.

class UserProfile(models.Model):
    img = models.ImageField(upload_to="imgs")
