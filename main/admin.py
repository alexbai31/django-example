from django.contrib import admin
from main.models import Person
from phones import settings
from twilio.rest import TwilioLookupsClient


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


