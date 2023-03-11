from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..course.serializers import CategorySerializer
from ..course.models import Category


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
