from django.urls import path, include

from .views import CategoryList

urlpatterns = [
    path('category/list/', CategoryList.as_view()),
]