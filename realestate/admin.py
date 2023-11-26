from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(PropertyInformation)
class PropertyInformationAdmin(admin.ModelAdmin):
    list_display = ('owner_name',)
    prepopulated_fields = {'slug': ('owner_name',)}
    
@admin.register(State)
class PropertyInformationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class PropertyInformationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PropertyModel)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PropertyPossibilities)
class PropertyPossibilitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TypeFloorProperty)
class TypeFloorPropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(HeatingSystemProperty)
class HeatingSystemPropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CoolingSystemProperty)
class CoolingSystemPropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SelectionSans)
class SelectionSansAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(KitchenEquipment)
class KitchenEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WelfarePossibilities)
class WelfarePossibilitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(EntertainmentPossibilities)
class EntertainmentPossibilitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OtherSpacesResidence)
class OtherSpacesResidenceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(EnvironmentalContext)
class EnvironmentalContextAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BedCount)
class BedCountAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TypeOwnership)
class TypeOwnershipAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Comment)