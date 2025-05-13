from modeltranslation.translator import translator, TranslationOptions
from properties.models import Property, Region, District, Amenities, Comment


class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description',
              'address',)

translator.register(Property, PropertyTranslationOptions)


class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Region, RegionTranslationOptions)


class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(District, DistrictTranslationOptions)

class AmenitiesTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Amenities, AmenitiesTranslationOptions)



