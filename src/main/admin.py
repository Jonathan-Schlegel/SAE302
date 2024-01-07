from django.contrib import admin
from authentication.models import CustomUser
from .models import Sender, Vehicle, Transport, Addressee, Package
from django.contrib.auth.admin import UserAdmin



admin.site.register(Sender)
admin.site.register(Transport)
admin.site.register(Addressee)
admin.site.register(Package)
