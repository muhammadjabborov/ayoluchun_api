from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

from ..account.models import Author
from ..common.models import BaseModel, GenderType, Region
from phonenumber_field.modelfields import PhoneNumberField


class Category(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(BaseModel):
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE, related_name='category_courses')
    # author = models.ForeignKey(Author, verbose_name=_(Author))