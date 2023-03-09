from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.blog.models import Category, Blog


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('id', 'name')
    fields = ('icon', 'name')


@admin.register(Blog)
class BlogModelAdmin(ModelAdmin):
    list_display = ('id', 'title', 'category_name')

    def category_name(self, obj):
        return obj.category.name

    category_name.short_description = 'Category'
