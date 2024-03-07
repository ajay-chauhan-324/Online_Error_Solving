from django.db import models

# Create your models here.
class user(models.Model):
  uname=models.CharField(max_length=122)
  Pass1=models.CharField(max_length=122)

  def __str__(self) :
      return self.st_name