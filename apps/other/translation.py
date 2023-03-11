from modeltranslation.translator import translator, TranslationOptions
from .models import Advertisement, RulesOfUse, Contact, Notification


class AdvertisementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Advertisement, AdvertisementTranslationOptions)


class RulesOfUseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(RulesOfUse, RulesOfUseTranslationOptions)


class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'address')


translator.register(Contact, ContactTranslationOptions)


class NotificationTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


translator.register(Notification, NotificationTranslationOptions)
