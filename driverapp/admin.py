from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BusInformation)
class BusInformationAdmin(admin.ModelAdmin):
    '''Admin View for BusInformation'''

    list_display = ('car_name','name_car_owner','device_color','device_type',)

admin.site.register(Color)
admin.site.register(CartTypes)
admin.site.register(DeviceTypes)
admin.site.register(Comment)