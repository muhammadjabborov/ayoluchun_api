from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CharField, SlugField, ForeignKey, CASCADE, IntegerField
from django.utils.translation import gettext_lazy as _
from thumbnails.fields import ImageField

from apps.common.models import BaseModel, AnnouncementView


class Category(BaseModel):
    icon = ImageField(upload_to='icons/Y%/m%/%d/')
    name = CharField(_('Name'), max_length=255)
    slug = SlugField(_('Slug'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']


class Blog(BaseModel):
    category = ForeignKey('blog.Category', CASCADE, _('Category'))
    title = CharField(_('Title'), max_length=255)
    slug = SlugField(_('Slug'), unique=True)
    author = ForeignKey('account.Author', CASCADE, _('Author'))
    photo = ImageField(_('Photo'), upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    views = IntegerField(default=0)
    description = RichTextField(_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']
