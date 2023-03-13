from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Category, Course, CourseView, Lesson, Content, ContentView, ContentComment, Certificate


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Course)
class CourseModelAdmin(ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'price', 'discount', 'rate')
    list_display_links = ("id", "title")
    list_filter = ('category', 'type', 'author')
    date_hierarchy = ("created_at")
    search_fields = ("id", "title", "price", "price", "discount", 'description')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(CourseView)
class CourseViewModelAdmin(ModelAdmin):
    list_display = ('id', 'course', 'device_id')
    list_display_links = ('id', 'course')
    list_filter = ('course',)


@admin.register(Lesson)
class LessonModelAdmin(ModelAdmin):
    list_display = ('id', 'course', 'title', 'order')
    list_display_links = ("id", "course")
    list_filter = ('course',)
    date_hierarchy = ("created_at")
    search_fields = ("id", "course", "title", "order", "description")


@admin.register(Content)
class ContentModelAdmin(ModelAdmin):
    list_display = ('id', 'lesson', 'title', 'order')
    list_display_links = ("id", "lesson")
    list_filter = ('lesson',)
    date_hierarchy = ("created_at")
    search_fields = ("id", "lesson", "title", "order")


@admin.register(ContentView)
class ContentViewModelAdmin(ModelAdmin):
    list_display = ('id', 'content', 'user', 'is_viewed')
    list_display_links = ('id', 'content')


@admin.register(ContentComment)
class ContentCommentModelAdmin(ModelAdmin):
    list_display = ('id', 'content', 'user', 'comment', 'parent')
    list_display_links = ('id', 'content')


@admin.register(Certificate)
class CertificateModelAdmin(ModelAdmin):
    list_display = ('id', 'course', 'user', 'file', 'rate', 'comment')
    list_display_links = ('id', 'course')
