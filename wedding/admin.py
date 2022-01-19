from django.contrib import admin
from wedding.models import User, Guest, Event, Invitation, Accomodations, Story, WeddingParty

# Register your models here.
admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(Accomodations)
admin.site.register(Story)
admin.site.register(WeddingParty)
