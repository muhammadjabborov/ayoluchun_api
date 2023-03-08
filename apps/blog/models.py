from django.db import models
from django.db.models import CharField

from apps.common.models import BaseModel


class Category(BaseModel):
    name = CharField()


class Blog(BaseModel):
    pass
