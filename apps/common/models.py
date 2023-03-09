from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from django.db import models
from django.db.models import Model, DateTimeField, SET_NULL, ForeignKey, CASCADE


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)  # noqa
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = "%s-%d" % (origin_slug, numb)
        numb += 1
    return unique_slug


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if hasattr(self, "slug") and hasattr(self, "title"):
            if not self.slug:
                self.slug = generate_unique_slug(self.__class__, self.title)

        if hasattr(self, "slug") and hasattr(self, "name"):
            if not self.slug:
                self.slug = generate_unique_slug(self.__class__, self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class AnnouncementView(BaseModel):
    device_id = models.CharField(max_length=100)
    blog = ForeignKey('blog.Blog', CASCADE)
    user = models.ForeignKey('account.User', SET_NULL, null=True, blank=True)


class GenderType(models.TextChoices):
    MALE = "Erkak"
    FEMALE = "Ayol"


class SalesType(models.TextChoices):
    BESTSELLER = "Bestseller"
    RECOMMENDED = "Tavsiya etilgan"


class PaymentType(models.TextChoices):
    PAYME = "Payme"
    APELSIN = "Apelsin"
    KPAY = "Kpay"
    CLICK = "Click"
    VISA = "Visa"
    MASTERCARD = "Mastercard"


class PaymentStatusType(models.TextChoices):
    SUCCESS = "Success"
    FAILED = "Failed"
    WAITING = "Waiting"


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
        verbose_name = "Region"
        verbose_name_plural = "Regions"
