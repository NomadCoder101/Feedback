from django.db import models

# Create your models here.

class User_Profile(models.Model):
    image = models.FileField(upload_to="images")