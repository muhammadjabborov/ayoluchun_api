from modeltranslation.translator import translator, TranslationOptions
from .models import User, Author, JobPosition


class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


translator.register(User, UserTranslationOptions)


class JobPositionTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(JobPosition, JobPositionTranslationOptions)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('address', 'job', 'bio')


translator.register(Author, AuthorTranslationOptions)
