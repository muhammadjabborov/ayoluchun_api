from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Author, JobPosition


class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "first_name", "last_name", "phone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    list_display_links = ("id", "username", "first_name", "phone")
    filter_horizontal = ("groups", "user_permissions")
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        (_("Personal Info"), {"fields": ("username", "email", "phone", "password")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "phone", "password1", "password2", "is_active", "is_staff",),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "region", "job")
    list_display_links = ("id", "user",)
    search_fields = ("user",)
    date_hierarchy = 'created_at'
    list_filter = ('position', 'region')


admin.site.register(Author, AuthorAdmin)


@admin.register(JobPosition)
class JobPositionModelAdmin(ModelAdmin):
    list_display = ('id', 'name')
