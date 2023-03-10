from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.common.models import Region, Country


@admin.register(Country)
class CountryModelAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Region)
class RegionModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'country_name')

    def country_name(self, obj):
        return obj.country.name

    country_name.short_description = 'Country'

