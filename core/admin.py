from django.contrib import admin
from core.models import Profile, Location, Address, Slip, Checkin


admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Address)
admin.site.register(Slip)
admin.site.register(Checkin)