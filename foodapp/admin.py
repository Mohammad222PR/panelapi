from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ChefInformation)
class BusInformationAdmin(admin.ModelAdmin):
    '''Admin View for BusInformation'''

    list_display = ('number',)


admin.site.register(CookType)
admin.site.register(Comment)