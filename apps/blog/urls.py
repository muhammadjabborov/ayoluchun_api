from django.urls import path

from apps.account.views import CreateAuthorAPIView, ListAuthorAPIView
from apps.blog.views import CreateCategoryAPIView, ListCategoryAPIView, BlogAPIView, UpdateCategoryAPIView, \
    RetrieveCategoryAPIView, DestroyCategoryAPIView, RetrieveBlogAPIView, UpdateBlogAPIView, DestroyBlogAPIView

urlpatterns = [
    path('blog/category/list/', ListCategoryAPIView.as_view()),
    path('blog/category/create/', CreateCategoryAPIView.as_view()),
    path('blog/category/update/<str:slug>/', UpdateCategoryAPIView.as_view()),
    path('blog/category/retrieve/<str:slug>/', RetrieveCategoryAPIView.as_view()),
    path('blog/category/delete/<str:slug>/', DestroyCategoryAPIView.as_view()),
    path('blog/', BlogAPIView.as_view()),
    path('blog/retrieve/<str:slug>/', RetrieveBlogAPIView.as_view()),
    path('blog/update/<str:slug>/', UpdateBlogAPIView.as_view()),
    path('blog/delete/<str:slug>/', DestroyBlogAPIView.as_view()),
    path('blog/author/create/', CreateAuthorAPIView.as_view()),
    path('blog/author/list/', ListAuthorAPIView.as_view())

]
