from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _

from ..account.models import Author
from ..common.models import BaseModel, SalesType, Region


class Category(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(BaseModel):
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE,
                                 related_name='category_courses')
    author = models.ForeignKey(Author, verbose_name=_(Author), on_delete=models.CASCADE, related_name='author_courses')
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    type = models.CharField(verbose_name="Sales type", max_length=25, choices=SalesType.choices, null=True, blank=True)
    rate = models.DecimalField(verbose_name='Rate', decimal_places=2, max_digits=5, default=0)
    photo = models.ImageField(verbose_name="Photo", upload_to="course/photo/%Y/%m/%d/")
    video = models.FileField(verbose_name="Photo", upload_to="course/video/%Y/%m/%d/")
    description = RichTextField()
    price = models.DecimalField(verbose_name=_('Price'), decimal_places=2, max_digits=10, default=0)
    discount = models.DecimalField(verbose_name=_('Discount'), decimal_places=2, max_digits=10, default=0, null=True,
                                   blank=True)
    views = models.IntegerField(verbose_name=_('Views'), default=0)
    ip = models.GenericIPAddressField(verbose_name=_('IP'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Lesson(BaseModel):
    cource = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE,
                               related_name='course_lessons')
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    rate = models.DecimalField(verbose_name=_('Rate'), max_digits=5, decimal_places=2)
    description = RichTextField(verbose_name=_('Description'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Content(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name=_('Lesson'), on_delete=models.CASCADE,
                               related_name='lesson_contents')
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    video = models.FileField(verbose_name=_('Video'), upload_to="curse/lesson/content/%Y/%m/%d/")
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"


class ContentViews(BaseModel):
    content = models.ForeignKey(Content, verbose_name=_('Content views'), on_delete=models.CASCADE,
                                related_name='content_views')
    user = models.ForeignKey('auth.User', verbose_name=_('User'), on_delete=models.CASCADE,
                             related_name='user_views_videos')
    is_viewed = models.BooleanField(verbose_name='Is viewed', default=False)

    def __str__(self):
        return self.content.title

    class Meta:
        verbose_name = "Content view"
        verbose_name_plural = "Content views"


class ContentComment(BaseModel):
    content = models.ForeignKey(Content, verbose_name=_('Content'), on_delete=models.CASCADE,
                                related_name='content_comments')
    user = models.ForeignKey('auth.User', verbose_name=_('User'), on_delete=models.CASCADE,
                             related_name='user_comments')
    comment = models.CharField(verbose_name=_('Comment'), max_length=255)
    parent = models.ForeignKey('self', verbose_name="Comment parent", null=True, blank=True, on_delete=models.CASCADE,
                               related_name='replies')

    def __str__(self):
        return self.content.title

    class Meta:
        verbose_name = "Content comment"
        verbose_name_plural = "Content comments"


class Certificate(BaseModel):
    cource = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE,
                               related_name='course_certificates')
    user = models.ForeignKey('auth.User', verbose_name=_('User'), on_delete=models.CASCADE,
                             related_name='user_certificates')
    file = models.FileField(verbose_name=_('File'), upload_to='course/certificate/%Y/%m/%d/')
    rate = models.DecimalField(verbose_name=_('Rate'), decimal_places=2, max_digits=5)
    comment = models.CharField(verbose_name=_('Comment'), max_length=255)

    def __str__(self):
        return self.cource.title

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
