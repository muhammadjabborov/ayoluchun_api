from django.urls import path

from .views import CategoryList, CategoryRetrieve, CourseList, CourseRetrieve, LessonList, CreateCertificate ,CertificateRetrieve

urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('category/<str:slug>', CategoryRetrieve.as_view()),
    path('course/list/', CourseList.as_view()),
    path('course/<str:slug>', CourseRetrieve.as_view()),
    path('lesson/list/<str:slug>', LessonList.as_view()),
    path('certificate/create/', CreateCertificate.as_view()),
    path('certificate/', CertificateRetrieve.as_view()),
]
