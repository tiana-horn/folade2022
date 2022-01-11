from django.shortcuts import render
from wedding.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

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

