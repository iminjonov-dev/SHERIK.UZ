from django.contrib import admin
from django.contrib.admin import ModelAdmin

from properties.models import Property, District, Region, Amenities, PropertyImage, Comment
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    list_display =('owner',
                   'title',
                   'description',
                   'district',
                   'address',
                   'latitude',
                   'longitude',
                   'rooms',
                   'floor',
                   'total_floor',
                   'area',
                   # 'amenities',
                   'furnished',
                   'price_day',
                   'price_week',
                   'price_year',
                   'status',
                   ) # Ko‘p-munosaabatlar uchun qulay interfeys


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ('name',)
@admin.register(District)
class DistrictAdmin(TranslationAdmin):
    list_display = ('name','region')

@admin.register(Amenities)
class AmenitiesAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(PropertyImage)
class AmenitiesAdmin(ModelAdmin):
    list_display = ('image','property',)

@admin.register(Comment)
class RegionAdmin(ModelAdmin):
    fields = ('user','comment','property')
