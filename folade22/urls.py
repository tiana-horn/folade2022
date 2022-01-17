"""folade22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from wedding import views as wedding_views
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', wedding_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('gallery/', wedding_views.gallery, name='gallery'),
    path('interest/', wedding_views.interest, name='interest'),
    path('party/', wedding_views.party, name='party'),
    path('registry/', wedding_views.registry, name='registry'),
    path('rsvp/<pk>', wedding_views.rsvp, name='rsvp'),
    path('findguest/', wedding_views.guest_list, name='findguest'),
    path('schedule/', wedding_views.schedule, name='schedule'),
    path('story/', wedding_views.story, name='story'),
    path('accomodations/', wedding_views.accomodations, name='accomodations'),
] 

handler400 = 'wedding.views.bad_request_view'
handler403 = 'wedding.views.permission_denied_view'
handler404 = 'wedding.views.page_not_found_view'
handler500 = 'wedding.views.error_view'


