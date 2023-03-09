from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from ..common.models import BaseModel


class Advertisement(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    photo = models.ImageField(verbose_name="Photo", upload_to="advertisement/%Y/%m/%d/")
    description = RichTextField(verbose_name=_('Description'))
    link = models.CharField(verbose_name=_('Link'), max_length=255)
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


class RulesOfUse(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "RulesOfUse"
        verbose_name_plural = "RulesOfUses"


class Contact(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone"), unique=True)
    email = models.EmailField(verbose_name=_('Email'))
    address = models.CharField(verbose_name=_('Address'), max_length=255)
    map = models.CharField(verbose_name=_('Map'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Message(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone"), unique=True)
    email = models.EmailField(verbose_name=_('Email'))
    msg = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Notification(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to="course/photo/%Y/%m/%d/")
    context = RichTextField(verbose_name=_("Context"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
