from django.urls import path

from apps.blog.views import CreateCategoryAPIView, ListCategoryAPIView, BlogAPIView, UpdateCategoryAPIView, \
    RetrieveCategoryAPIView, DestroyCategoryAPIView, RetrieveBlogAPIView

urlpatterns = [
    path('category/list/', ListCategoryAPIView.as_view()),
    path('category/create/', CreateCategoryAPIView.as_view()),
    path('category/update/<str:slug>/', UpdateCategoryAPIView.as_view()),
    path('category/retrieve/<str:slug>/', RetrieveCategoryAPIView.as_view()),
    path('category/delete/<str:slug>/', DestroyCategoryAPIView.as_view()),

    path('blog/', BlogAPIView.as_view()),
    path('blog/retrieve/<str:slug>/', RetrieveBlogAPIView.as_view())

]
