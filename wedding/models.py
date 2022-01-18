from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    rsvped = models.BooleanField(default=False)

class Guest(models.Model):
    name = models.CharField(max_length=111)
    email = models.EmailField(max_length=111,blank=True)
    dietary= models.CharField(max_length=777,blank=True)
   
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=222)
    date = models.DateField()
    time = models.CharField(max_length=222)
    location = models.CharField(max_length=777)
    guests = models.ManyToManyField(Guest, through='Invitation')

    def __str__(self):
        return self.name

class Invitation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)



