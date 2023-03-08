from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    class Meta:
        abstract = True


class GenderType(models.TextChoices):
    MALE = "Erkak"
    FEMALE = "Ayol"


class SalesType(models.TextChoices):
    BESTSELLER = "Bestseller"
    RECOMMENDED = "Tavsiya etilgan"


class Country(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Region(models.Model):
    country = models.ForeignKey(Country, verbose_name=_('Country'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"