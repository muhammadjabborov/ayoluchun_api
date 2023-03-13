from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.other.models import Advertisement, RulesOfUse, Contact, Message, Notification


@admin.register(Advertisement)
class AdvertisementModelAdmin(ModelAdmin):
    list_display = ('id', 'title')


@admin.register(RulesOfUse)
class RulesOfUseModelAdmin(ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Contact)
class ContactModelAdmin(ModelAdmin):
    list_display = ('id', 'title', 'phone')


@admin.register(Message)
class MessageModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'phone')


@admin.register(Notification)
class NotificationModelAdmin(ModelAdmin):
    list_display = ('id', 'title')
