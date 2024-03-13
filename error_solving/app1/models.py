from django.db import models

# Create your models here.
class User(models.Model):
  uname=models.CharField(max_length=122)
  email=models.EmailField(max_length=254)
  Pass1=models.CharField(max_length=122)

  def __str__(self) :
      return self.uname