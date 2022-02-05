from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError

DIET_CHOICES = (
    ('none','none'),
    ('vegan','vegan'),
    ('vegetarian','vegetarian'),
)

# Create your models here.
class User(AbstractUser):
    rsvped = models.BooleanField(default=False)

class Song(models.Model):
    page = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.URLField(unique=False, blank=True)

    def __str__(self):
         return f'{self.page} - {self.title}'

class Guest(models.Model):
    name = models.CharField(max_length=111)
    email = models.EmailField(max_length=111,blank=True)
    aso_ebi = models.BooleanField(default=False,blank=True)
    aso_ebi_paid = models.BooleanField(default=False,blank=True)
    hotel_accomodations = models.BooleanField(default=False,blank=True)
    diet = models.CharField(
        max_length=10, null=True, blank=True, choices=DIET_CHOICES,default='none')
    food_allergies= models.CharField(max_length=777,blank=True)
   
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=222)
    description = models.CharField(max_length=222,blank=True)
    date = models.DateField()
    time = models.CharField(max_length=222)
    location = models.CharField(max_length=777)
    address = models.CharField(null=True,max_length=777)
    guests = models.ManyToManyField(Guest, through='Invitation')

    def __str__(self):
        return self.name

class Invitation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attending = models.BooleanField()
    def __str__(self):
        return f'{self.guest} - {self.event}'

class Plus_One(models.Model):
    name = models.CharField(max_length=111)
    accompanying = models.ForeignKey(Invitation, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Accomodation(models.Model):
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111,blank=True)
    location = models.CharField(max_length=777,blank=True)
    phone = models.CharField(max_length=77,blank=True)
    block_name = models.CharField(max_length=77,blank=True)
    block_rate = models.CharField(max_length=77,blank=True)
    detail = models.TextField(max_length=777,blank=True)
    link = models.URLField(unique=False, blank=True)
    deadline = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.title

class Travel(models.Model):
    location = models.CharField(max_length=222)
    detail = models.TextField(max_length=1111,blank=True)
    departure_time = models.TextField(max_length=1111,blank=True)
    venue_distance = models.CharField(max_length=222,blank=True)
    downtown_distance = models.CharField(max_length=222,blank=True)
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111,blank=True)


    def __str__(self):
        return self.location

class StoryText(models.Model):
    image1 = models.ImageField(upload_to='img', null=True)
    image1_alt_text = models.CharField(max_length=111)
    p1_story_owner = models.CharField(null=True,max_length=222)
    p2_story_owner = models.CharField(null=True,max_length=222)
    p1_part1 = models.TextField(max_length=77777)
    p1_bold = models.CharField(max_length=777)
    p1_part2 = models.TextField(max_length=77777)
    p2_part1 = models.TextField(max_length=77777)
    p2_bold = models.CharField(max_length=777)
    p2_part2 = models.TextField(max_length=77777)
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
    bridal_side = models.BooleanField(default=False,null=True)
    groom_side = models.BooleanField(default=False,null=True)
    description = models.TextField(max_length=777,blank=True)
    order = models.IntegerField(null=True)

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

class Host(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111)
    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    role = models.CharField(max_length=222)
    description = models.TextField(max_length=777,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class FAQ(models.Model):
    question = models.TextField(max_length=1111)
    answer = models.TextField(max_length=1111)
    
    def __str__(self):
        return self.question

class Scripture(models.Model):
    scripture = models.TextField(max_length=1111)
    source = models.TextField(max_length=1111)
    
    def __str__(self):
        return self.source 

class ComingSoon(models.Model):
    host_page = models.BooleanField(default=False)
    story_page = models.BooleanField(default=False)
    party_page = models.BooleanField(default=False)
    registry_page = models.BooleanField(default=False)
    rsvp_page = models.BooleanField(default=False)
    
    def clean(self):
        if ComingSoon.objects.exists() and not self.pk:
            raise ValidationError('There can only be one coming soon flag in the database')

class WeddingPartyCarouselImage(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111) 
    caption = models.CharField(max_length=111) 

    def __str__(self):
        return self.image_alt_text

class BannerImage(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    image_alt_text = models.CharField(max_length=111) 
    schedule_page = models.BooleanField(default=False)
    registry_page = models.BooleanField(default=False)
    faq_page = models.BooleanField(default=False)

class HomeImage(models.Model):
    image1mobile = models.ImageField(upload_to='img', null=True, blank=True)
    image1mobile_alt_text = models.CharField(max_length=111,null=True, blank=True) 
    image2mobile = models.ImageField(upload_to='img', null=True, blank=True)
    image2mobile_alt_text = models.CharField(max_length=111, blank=True) 
    image3mobile = models.ImageField(upload_to='img', null=True, blank=True)
    image3mobile_alt_text = models.CharField(max_length=111, blank=True) 
    image1desktop = models.ImageField(upload_to='img', null=True, blank=True)
    image1desktop_alt_text = models.CharField(max_length=111, null=True, blank=True) 
    image2desktop = models.ImageField(upload_to='img', null=True, blank=True)
    image2desktop_alt_text = models.CharField(max_length=111, blank=True) 
    image3desktop = models.ImageField(upload_to='img', null=True, blank=True)
    image3desktop_alt_text = models.CharField(max_length=111, blank=True) 

class MassUpload(models.Model):
    guest_list = models.FileField()
    invitation_list = models.FileField()
