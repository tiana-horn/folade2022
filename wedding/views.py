import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from wedding.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from wedding.forms import InterestForm
import boto3
import json

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

def gallery(request):
    return render(request, 'gallery.html')

def party(request):
    return render(request, 'party.html')

def registry(request):
    return render(request, 'registry.html')

def rsvp(request):
    return render(request, 'rsvp.html')

def schedule(request):
    return render(request, 'schedule.html')

def story(request):
    return render(request, 'story.html')

def accomodations(request):
    return render(request, 'accomodations.html')

