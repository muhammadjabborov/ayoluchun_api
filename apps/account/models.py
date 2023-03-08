from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .account_manager import AccountManager
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from ..common.models import BaseModel, GenderType, Region
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("Email"), max_length=60, unique=True, null=True)
    username = models.CharField(verbose_name=_("Username"), max_length=30, unique=True)
    phone = PhoneNumberField(verbose_name=_("Phone"), unique=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=30)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=30)
    birthday = models.DateTimeField(verbose_name=_('Birthday'), null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GenderType.choices, default=GenderType.FEMALE)
    is_gmail_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name=_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(verbose_name=_("last login"), auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class JobPosition(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Position"
        verbose_name_plural = "Job Positions"


class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))

    photo = models.ImageField(verbose_name=_("Photo"), upload_to='authors', default='user.png', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),)
    bio = RichTextField(verbose_name=_("About author"))
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
