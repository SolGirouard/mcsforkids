from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
   name = models.CharField(max_length=200)
   origin = models.CharField(max_length=200)
   description = models.TextField()
   imageURL = models.URLField()
   buyURL = models.URLField()
   price = models.DecimalField(max_digits=6, decimal_places=2)
   minAge = models.PositiveSmallIntegerField(default=5)
   maxAge = models.PositiveSmallIntegerField(default=15)
   dateAdded = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.name
