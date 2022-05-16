from django.db import models

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField(max_length=100)
    description = models.TextField(max_length=250)

