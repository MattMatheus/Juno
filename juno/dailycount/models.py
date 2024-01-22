from django.db import models


# Create your models here.
class FoodItem(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    mood = models.CharField(max_length=200, default="none")
