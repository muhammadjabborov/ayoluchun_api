from modeltranslation.translator import translator, TranslationOptions
from .models import Country, Region


class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Country, CountryTranslationOptions)


class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Region, RegionTranslationOptions)
