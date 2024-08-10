from django.contrib import admin
from core.models import Profile, Location, Address, Slip, Checkin, LocationNotMember

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'score']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'score']
    ordering = ['-user']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'ชื่อจริง'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'นามสกุล'

class LocationAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'lat', 'lng', 'timestamp', 'map_link']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'lat', 'lng']
    ordering = ['-timestamp']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'ชื่อจริง'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'นามสกุล'

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'address_line', 'province', 'district', 'postal_code']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'address_line', 'province', 'district', 'postal_code']
    ordering = ['-user']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'ชื่อจริง'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'นามสกุล'

class SlipAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'cost', 'approve', 'timestamp']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'cost']
    list_filter = ['approve', 'timestamp']
    ordering = ['-timestamp']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'ชื่อจริง'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'นามสกุล'

class CheckinAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'checkin', 'checkin_time', 'des']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'checkin_time', 'des']
    list_filter = ['checkin', 'checkin_time']
    ordering = ['-checkin_time']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'ชื่อจริง'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'นามสกุล'

class LocationNotMemberAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "lat", "lng", "map_link", "timestamp"]
    search_fields = ["name", "timestamp"]
    ordering = ["-timestamp"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Slip, SlipAdmin)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(LocationNotMember, LocationNotMemberAdmin)
