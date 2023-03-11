from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Blog


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Blog, BlogTranslationOptions)
