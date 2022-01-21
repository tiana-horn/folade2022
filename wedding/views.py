import gspread
from django.contrib.auth import authenticate
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from wedding.models import User, Guest, Event, Invitation, Accomodation, StoryText, WeddingPartyMember, RegistryLink, GalleryImage, Host, FAQ, Travel, Song, Scripture
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from wedding.forms import InterestForm, AccessForm, SearchForm, GuestForm
from lockdown.decorators import lockdown
import boto3
import json
import os

# Create your views here.
def home(request):
    song = Song.objects.get(page="home")
    return render(request, 'home.html',{
        'song':song,
    })

def interest(request):
    form = InterestForm

    #Code to Google Sheet

    #Code to get Google APIs secret manager key
    secret_name = "client_secret"
    region_name = "us-east-2"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    if 'SecretString' in get_secret_value_response:
        secret = json.loads(get_secret_value_response['SecretString'])
        secret2 = json.loads(secret.get('client_secret', ''))
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(secret2, scope)
    client = gspread.authorize(creds)
    
    if request.method == 'POST':
        form = form(data=request.POST)

        #Get the variables for the email from the form
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Phone = form.cleaned_data['Phone']
            Street_Address = form.cleaned_data['Street_Address']
            Street_Address_Line_2 = form.cleaned_data['Street_Address_Line_2']
            City = form.cleaned_data['City']
            State = form.cleaned_data['State']
            Country = form.cleaned_data['Country']
            Zipcode = form.cleaned_data['Zipcode']

            try:
                row = [Name,Email,Phone,Street_Address,Street_Address_Line_2,City,State,Country,Zipcode]
                sheet = client.open("Interest Form Sign Up").sheet1
                sheet.insert_row(row)

    # Show success message, if other messages are added update conditional on index
                django_message = "Thank you for expressing interest in attending our wedding! Someone will be in contact with you shortly"
                messages.add_message(request, messages.INFO, django_message)
            except:
                Http404

            return redirect('interest')

    return render(request, 'interest.html', {
        'form': form,
    })

@lockdown()
def gallery(request):
    song = Song.objects.get(page="gallery")
    pictures = GalleryImage.objects.all()
    return render(request, 'gallery.html', {
        'pictures':pictures,
        'song':song,
    })

@lockdown()
def party(request):
    party = WeddingPartyMember.objects.all()
    song = Song.objects.get(page="party")

    return render(request, 'party.html', {
        'party':party,
        'song':song,
    })

@lockdown()
def registry(request):
    registry_links = RegistryLink.objects.all()
    return render(request, 'registry.html', {
        'registry_links':registry_links,
    })

@lockdown()
def rsvp(request,pk):
    guest = Guest.objects.get(pk=pk)
    invites = Invitation.objects.filter(guest=guest)
    invites = invites.order_by('event')
    guest_form = GuestForm

    if request.method == 'POST':
        guest_form = guest_form(data=request.POST, instance=guest)
        if guest_form.is_valid():
            food_allergies = guest_form.cleaned_data['food_allergies']
            guest_form.save()
            django_message = "Thank you for your response!"
            messages.add_message(request, messages.SUCCESS, django_message)
            return redirect('success')
    else:   
        guest_form = guest_form(instance=guest)

    return render(request, 'rsvp.html', {
        'guest_form': guest_form,
        'guest':guest,
        'invites':invites,
    })
  

@lockdown()
def change_rsvp(request, pk):
    invite = Invitation.objects.get(pk=pk)
    guest = invite.guest
    if request.method == "POST":
        if invite.attending==True:
            invite.attending=False
            invite.save()
            return redirect('rsvp', pk=guest.pk)

        else: 
            invite.attending=True
            invite.save()
            return redirect('rsvp', pk=guest.pk)

            
    return render(request, 'rsvp.html', {
            'guest':guest,
            'invite':invite,
    })

@lockdown()
def guest_list(request):
    form = SearchForm
    searchresults = False
    notFound = False

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            try: 
                searchresults = Guest.objects.filter(name=name)
                print(searchresults)
                if len(searchresults) < 1 :
                    notFound = "Sorry, we couldn't find your name. Please check your invitation or contact Fola & Lade if you think there is an error"
            except:
                pass

    return render(request, 'findguest.html',{
        'form':form,    
        'searchresults':searchresults,
        'notFound':notFound,
        })

@lockdown()
def success(request):
    return render(request, 'success.html')

@lockdown()
def schedule(request):
    events = Event.objects.all()
    song = Song.objects.get(page="schedule")

    return render(request, 'schedule.html', {
        'events':events,
        'song':song,
    })

@lockdown()
def story(request):
    story = StoryText.objects.all()
    song = Song.objects.get(page="story")

    return render(request, 'story.html', {
        'story':story,
        'song':song,
    })

@lockdown()
def accomodations(request):
    accomodations = Accomodation.objects.all()
    travels = Travel.objects.all()
    song = Song.objects.get(page="accomodations")
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(6,9):
        scriptures.append(scripture_list[i])

    return render(request, 'accomodations.html', {
        'accomodations':accomodations,
        'travels':travels,
        'song':song,
        'scriptures':scriptures,
    })

@lockdown()
def faq(request):
    faqs = FAQ.objects.all()
    song = Song.objects.get(page="faq")
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3,6):
        scriptures.append(scripture_list[i])

    return render(request, 'faq.html', {
        'faqs':faqs,
        'song':song,
        'scriptures':scriptures,
    })

@lockdown()
def hosts(request):
    hosts = Host.objects.all()
    song = Song.objects.get(page="hosts")
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3):
        scriptures.append(scripture_list[i])


    return render(request, 'hosts.html', {
        'hosts':hosts,
        'song':song,
        'scriptures':scriptures,
    })

def bad_request_view(request, exception):
    return render(request, '400.html', status=400)

def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def error_view(request):
    return render(request, '500.html', status=500)
