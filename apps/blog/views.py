from django.db.models import F
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, \
    DestroyAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.blog.models import Category, Blog
from apps.blog.serializers import CreateCategoryModelSerializer, CategoryModelSerializer, BlogModelSerializer, \
    ListBlogModelSerializer, RetrieveBlogModelSerializer
from apps.common.models import AnnouncementView


class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryModelSerializer
    parser_classes = (MultiPartParser,)
    # permission_classes = (IsAuthenticated,)


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.order_by('-created_at')
    serializer_class = CategoryModelSerializer
    parser_classes = (MultiPartParser,)
    # permission_classes = (IsAuthenticated,)


class RetrieveCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)
    # permission_classes = (IsAuthenticated,)


class DestroyCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)
    # permission_classes = (IsAuthenticated,)


class BlogAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    parser_classes = (MultiPartParser,)

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        queryset = self.queryset.order_by('-created_at')
        serializer = ListBlogModelSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class RetrieveBlogAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    parser_classes = (MultiPartParser,)
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        blog = get_object_or_404(queryset, slug=self.kwargs["slug"])
        if self.request.user.is_authenticated:
            AnnouncementView.objects.update_or_create(
                blog=blog,
                user=self.request.user,
            )
        elif self.request.headers.get("device-id", None):
            AnnouncementView.objects.update_or_create(
                blog=blog,
                device_id=self.request.headers.get("device-id", None),
            )

        return queryset
