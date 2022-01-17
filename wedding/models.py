from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    rsvped = models.BooleanField(default=False)

class Guest(models.Model):
    fullName = models.CharField(max_length=111)
    email = models.EmailField(max_length=111,blank=True)
    attending = models.BooleanField(default=False)
    dietary= models.TextField(max_length=777,blank=True)
   
    def __str__(self):
        return self.fullName



