from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError



# Create your models here.
class User(AbstractUser):
    rsvped = models.BooleanField(default=False)

class Guest(models.Model):
    name = models.CharField(max_length=111)
    email = models.EmailField(max_length=111,blank=True)
    food_allergies= models.CharField(max_length=777,blank=True)
   
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
    attending = models.BooleanField()

    def __str__(self):
        return f'{self.guest} - {self.event}'

class Accomodation(models.Model):
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111)
    location = models.CharField(max_length=777)
    detail = models.TextField(max_length=777)
    link = models.URLField(unique=False, blank=True)

    def __str__(self):
        return self.title

class StoryText(models.Model):
    image1 = models.ImageField(upload_to='img', null=True)
    image1_alt_text = models.CharField(max_length=111)
    p1_part1 = models.TextField(max_length=1111)
    p1_bold = models.CharField(max_length=222)
    p1_part2 = models.TextField(max_length=1111)
    p2_part1 = models.TextField(max_length=1111)
    p2_bold = models.CharField(max_length=222)
    p2_part2 = models.TextField(max_length=1111)
    image2 = models.ImageField(upload_to='img', null=True)
    image2_alt_text = models.CharField(max_length=111)


    def clean(self):
        if StoryText.objects.exists() and not self.pk:
            raise ValidationError('The Story page can only have one story. Please edit the existing story object to make changes')

class WeddingPartyMember(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111)
    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    role = models.CharField(max_length=222)
    description = models.TextField(max_length=777,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class RegistryLink(models.Model):
    zolaLink = models.URLField(unique=False, blank=True)
    zola_data_registry_key = models.CharField(max_length=222,blank=True)
    
    def clean(self):
        if RegistryLink.objects.exists() and not self.pk:
            raise ValidationError('The Registry page can only have one zola connected. Please edit the existing link to make changes')

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111) 
    
    def __str__(self):
        return self.image_alt_text
