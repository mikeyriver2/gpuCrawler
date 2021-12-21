from django.db import models

# Create your models here.

class Listing(models.Model):
  id = models.AutoField(primary_key=True) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  url = models.CharField(max_length=2048)
  name = models.CharField(max_length=350)
  price = models.FloatField()

  def __str__(self):
    return self.name