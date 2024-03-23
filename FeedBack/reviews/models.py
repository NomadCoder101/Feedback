from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator,MaxLengthValidator

# Create your models here.

class Review(models.Model):
    
    user_name=models.CharField(max_length=100)
    review_text=models.TextField()
    rating=models.IntegerField(validators=[
        MinValueValidator(1, message=None),
        MaxValueValidator(5, message=None),

    ])
    
    def __str__(self):
        return self.user_name


