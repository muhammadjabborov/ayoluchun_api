from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Course, Lesson, Content


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)


class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Course, CourseTranslationOptions)


class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Lesson, LessonTranslationOptions)


class ContentTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Content,)
