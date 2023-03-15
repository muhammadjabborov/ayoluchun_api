from unicodedata import name

from django.urls import path

from .views import CategoryList, CategoryRetrieve, CourseList, CourseRetrieve, LessonList, CreateCertificate, \
    CertificateRetrieve, CreateContentView, CreateContentComment

urlpatterns = [
    path('course/category/list/', CategoryList.as_view()),
    path('course/category/<str:slug>', CategoryRetrieve.as_view(), name='category-retrieve'),
    path('course/list', CourseList.as_view()),
    path('course/<str:slug>', CourseRetrieve.as_view()),
    path('course/lesson/list/<str:slug>', LessonList.as_view()),
    path('course/certificate/create/', CreateCertificate.as_view()),
    path('course/certificate/', CertificateRetrieve.as_view()),
    path('course/create-content-view/', CreateContentView.as_view()),
    path('course/create-content-comment/', CreateContentComment.as_view()),
]
