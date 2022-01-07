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
from django.views.generic import RedirectView

urlpatterns = [
    path('', wedding_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('gallery/', wedding_views.gallery, name='gallery'),
    path('party/', wedding_views.party, name='party'),
    path('registry/', wedding_views.registry, name='registry'),
    path('rsvp/', wedding_views.rsvp, name='rsvp'),
    path('schedule/', wedding_views.schedule, name='schedule'),
    path('story/', wedding_views.story, name='story'),
    path('travel/', wedding_views.travel, name='travel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

