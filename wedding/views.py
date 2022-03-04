import gspread
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from wedding.models import User, Guest, Event, Invitation, Accomodation, StoryText, WeddingPartyMember, RegistryLink, GalleryImage, Host, FAQ, Travel, Song, Scripture, ComingSoon, WeddingPartyCarouselImage, BannerImage,Plus_One,HomeImage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from wedding.forms import InterestForm, AccessForm, SearchForm, GuestForm, PlusOneForm, DeleteGuestsForm
from lockdown.decorators import lockdown
from collections import defaultdict
import boto3
import json
import os

# Create your views here.
def home(request):
    content = HomeImage.objects.all()
    song = Song.objects.get(page="home")
    return render(request, 'home.html',{
        'song':song,
        'content':content,
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
                django_message = "Thank you for expressing interest in attending our wedding! Someone will be in contact with you shortly."
                messages.add_message(request, messages.INFO, django_message)
            except:
                django_message = "We're sorry, we were unable to capture your submission. Please try again or contact Fola and Lade if the problem persists."
                messages.add_message(request, messages.INFO, django_message)

            return redirect('interest')

    return render(request, 'interest.html', {
        'form': form,
    })

@lockdown()
def gallery(request):
    song = Song.objects.get(page="gallery")
    pictures = GalleryImage.objects.all()
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3,6):
        scriptures.append(scripture_list[i])

    return render(request, 'gallery.html', {
        'pictures':pictures,
        'song':song,
        'scriptures':scriptures,

    })

@lockdown()
def party(request):
    party = WeddingPartyMember.objects.all().order_by('order')
    song = Song.objects.get(page="party")
    dev_flag = ComingSoon.objects.all()
    carouselpics = WeddingPartyCarouselImage.objects.all()
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3):
        scriptures.append(scripture_list[i])
    return render(request, 'party.html', {
        'party':party,
        'song':song,
        'dev_flag':dev_flag,
        'carouselpics':carouselpics,
        'scriptures':scriptures,

    })

@lockdown()
def registry(request):
    registry_links = RegistryLink.objects.all()
    dev_flag = ComingSoon.objects.all()
    banner = BannerImage.objects.all()
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(6,9):
        scriptures.append(scripture_list[i])
    return render(request, 'registry.html', {
        'registry_links':registry_links,
        'dev_flag':dev_flag,
        'banner':banner,
        'scriptures':scriptures,

    })

@lockdown()
def plus_one(request, pk):
    invite = Invitation.objects.get(pk=pk)
    guest = invite.guest

    if request.method == "POST":
        plus_one_form = PlusOneForm(request.POST)
        if plus_one_form.is_valid():
            plus_one = plus_one_form.save(commit=False)
            plus_one.name = plus_one_form.cleaned_data['name']
            plus_one.accompanying = invite
            plus_one.save()
            return redirect('rsvp', pk=guest.pk, name=guest.name)

        else: 
            plus_one_form = plus_one_form(instance=invite)
            extra_guests = Plus_One.objects.all()
    return render(request, 'rsvp.html', {
            'invite':invite,
            'plus_one_form':PlusOneForm(),
            'extra_guest':extra_guests,
    })

@lockdown()
def rsvp(request,pk,name):
    guest = Guest.objects.get(pk=pk)
    invites = Invitation.objects.filter(guest=guest)
    invites = invites.order_by('event')
    extra_guests = Plus_One.objects.all()
    guest_form = GuestForm
    plus_one_form = PlusOneForm
    if request.method == 'POST':
        guest_form = guest_form(data=request.POST, instance=guest)
        if guest_form.is_valid():
            diet = guest_form.cleaned_data['diet']
            food_allergies = guest_form.cleaned_data['food_allergies']
            guest_form.save()
            return redirect('success')
    else:   
        guest_form = guest_form(instance=guest)

    return render(request, 'rsvp.html', {
        'guest_form': guest_form,
        'guest':guest,
        'invites':invites,
        'extra_guests':extra_guests,
        'plus_one_form':plus_one_form,
    })
  

@lockdown()
def change_rsvp(request, pk):
    invite = Invitation.objects.get(pk=pk)
    guest = invite.guest
    if request.method == "POST":
        if invite.attending==True:
            invite.attending=False
            invite.save()
            return redirect('rsvp', pk=guest.pk, name=guest.name)

        else: 
            invite.attending=True
            invite.save()
            return redirect('rsvp', pk=guest.pk, name=guest.name)

            
    return render(request, 'rsvp.html', {
            'guest':guest,
            'invite':invite,
    })



@lockdown()
def guest_list(request):
    form = SearchForm
    searchresults = False
    notFound = False
    dev_flag = ComingSoon.objects.all()

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            try: 
                searchresults = Guest.objects.filter(name__iexact=name)
                if len(searchresults) < 1 :
                    notFound = "Sorry, we couldn't find your name. Please double check your invitation, contact Fola & Lade, or enter your information on our interest page if you think there is an error. "                          

            except:
                pass

    return render(request, 'findguest.html',{
        'form':form,    
        'searchresults':searchresults,
        'notFound':notFound,
        'dev_flag':dev_flag,

        })

@lockdown()
def success(request):
    return render(request, 'success.html')

@lockdown()
def schedule(request):
    events = Event.objects.all()
    song = Song.objects.get(page="schedule")
    banner = BannerImage.objects.all()
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3):
        scriptures.append(scripture_list[i])
    return render(request, 'schedule.html', {
        'events':events,
        'song':song,
        'banner':banner,
        'scriptures':scriptures,

    })



@lockdown()
def story(request):
    story = StoryText.objects.all()
    song = Song.objects.get(page="story")
    dev_flag = ComingSoon.objects.all()

    return render(request, 'story.html', {
        'story':story,
        'song':song,
        'dev_flag':dev_flag,
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
    banner = BannerImage.objects.all()

    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3,6):
        scriptures.append(scripture_list[i])

    return render(request, 'faq.html', {
        'faqs':faqs,
        'song':song,
        'scriptures':scriptures,
        'banner':banner,
    })

@lockdown()
def hosts(request):
    hosts = Host.objects.all()
    song = Song.objects.get(page="hosts")
    dev_flag = ComingSoon.objects.all()
    scripture_list = Scripture.objects.all()
    scriptures = []
    for i in range(3):
        scriptures.append(scripture_list[i])


    return render(request, 'hosts.html', {
        'hosts':hosts,
        'song':song,
        'scriptures':scriptures,
        'dev_flag':dev_flag,
    })

@lockdown()
@login_required
def responses(request):
    if request.user.is_superuser:
        invitations = Invitation.objects.all()
        events = Event.objects.all()
        plus_ones = Plus_One.objects.all()
        guests = Guest.objects.all()
        yesses = defaultdict(int)
        hotel = dict(block=0)
        aso = dict(interested=0)
        paid = dict(paid=0)
        not_paid = dict(not_paid=0)
        no_allergies = ['False','None','na','NA','N/A','No','none','no','Falsenone']

        for guest in guests:
            if guest.hotel_accomodations == True:
                hotel['block']+=1
            if guest.aso_ebi == True:
                aso['interested']+=1
                if guest.aso_ebi_paid == False:
                    not_paid['not_paid']+=1
            if guest.aso_ebi_paid == True:
                paid['paid']+=1
        
        for invite in invitations:
            if invite.attending==True:
                yesses[invite.event.name]+= 1
        yesses_dict = dict(yesses)

        for person in plus_ones:
            for x in list(yesses_dict):
                if person.accompanying.event.name == x:
                    yesses[x]+= 1
        yesses_dict = dict(yesses)

        return render(request, 'responses.html',{
            'invitations':invitations,
            'events':events,
            'guests':guests,
            'yesses':yesses,
            'yesses_dict':yesses_dict,
            'plus_ones':plus_ones,
            'hotel':hotel,
            'aso':aso,
            'paid':paid,
            'not_paid':not_paid,
            'no_allergies':no_allergies,
        })

@lockdown()
@login_required
def delete_guest(request, pk):
    if request.user.is_superuser:

        person = Plus_One.objects.get(pk=pk)
        invitation = person.accompanying

        if request.method == "POST":
            person.delete()
          
    return redirect('rsvp', pk=invitation.guest.pk, name=invitation.guest.name)

@lockdown()
@login_required
def upload(request):
    if request.user.is_superuser:
        delete_all_guests = DeleteGuestsForm
        if request.method == 'POST':
            delete_all_guests = delete_all_guests(data=request.POST)
            if delete_guests.is_valid():
                sure = delete_guests.form.cleaned_data['sure']
                if sure == True:
                    Guest.objects.all().delete()
                else:
                    pass
        else:
            delete_all_guests = DeleteGuestsForm

    return render(request, 'upload.html', {
        'delete_all_guests':delete_all_guests,
    })

def bad_request_view(request, exception):
    return render(request, '400.html', status=400)

def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def error_view(request):
    return render(request, '500.html', status=500)
