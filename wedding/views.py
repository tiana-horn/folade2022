import gspread
from django.contrib.auth import authenticate
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from wedding.models import User, Guest
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from wedding.forms import InterestForm, AccessForm, SearchForm, GuestForm
from lockdown.decorators import lockdown
from wedding.filters import GuestFilter
import boto3
import json
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
                messages.add_message(request, messages.SUCCESS, django_message)
            except:
                Http404

            return redirect('interest')

    return render(request, 'interest.html', {
        'form': form,
    })

@lockdown()
def gallery(request):
    return render(request, 'gallery.html')

@lockdown()
def party(request):
    return render(request, 'party.html')

@lockdown()
def registry(request):
    return render(request, 'registry.html')

@lockdown()
def rsvp(request,pk):
    guest = Guest.objects.get(pk=pk)
    form_class = GuestForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=guest)
        if form.is_valid():
            form.save()
            django_message = "Thank you for your response!"
            messages.add_message(request, messages.SUCCESS, django_message)
            return redirect('rsvp', pk=guest.pk)
    else:   
        form = form_class(instance=guest)
        return render(request, 'rsvp.html', {
            'form': form,
            'guest':guest,
        })

@lockdown()
def guest_list(request):
    form = SearchForm
    searchresults = False

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            fullName = form.cleaned_data['fullName']
            try: 
                searchresults = Guest.objects.filter(fullName=fullName)
            except:
                django_message = "We couldn't find your name, please check your invitation or contact Fola & Lade if you think there is an error"
                messages.add_message(request, messages.ERROR, django_message)


    return render(request, 'findguest.html',{
        'form':form,    
        'searchresults':searchresults,
        })

@lockdown()
def schedule(request):
    return render(request, 'schedule.html')

@lockdown()
def story(request):
    return render(request, 'story.html')

@lockdown()
def accomodations(request):
    return render(request, 'accomodations.html')

def bad_request_view(request, exception):
    return render(request, '400.html', status=400)

def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def error_view(request):
    return render(request, '500.html', status=500)
