from django.contrib import admin
from wedding.models import User, Guest, Event, Invitation

# Register your models here.
admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(Invitation)
