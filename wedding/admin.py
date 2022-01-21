from django.contrib import admin
from wedding.models import User, Guest, Event, Invitation, Accomodation, StoryText, WeddingPartyMember, RegistryLink, GalleryImage, Travel, FAQ, Host, Song, Scripture, ComingSoon

# Register your models here.
admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(Accomodation)
admin.site.register(StoryText)
admin.site.register(WeddingPartyMember)
admin.site.register(RegistryLink)
admin.site.register(GalleryImage)
admin.site.register(Travel)
admin.site.register(FAQ)
admin.site.register(Host)
admin.site.register(Song)
admin.site.register(Scripture)
admin.site.register(ComingSoon)

