from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    rsvped = models.BooleanField(default=False)

# class Guest(models.Model):
#     rsvp = models.BooleanField(default=False)
#     full_name = models.CharField(max_length=111)
#     email = models.EmailField(max_length=333)
#     phone= models.CharField(max_length=111)
#     street_address = models.CharField(max_length=333)
#     street_address_line_2 = models.CharField(max_length=333)
#     city = models.CharField(max_length=333)
#     state = models.CharField(max_length=333)
#     country = models.CharField(max_length=333)
#     zipcode models.CharField(max_length=111)

#     def __str__(self):
#         return self.full_name



