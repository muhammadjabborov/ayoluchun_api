from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, \
    DestroyAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.blog.models import Category, Blog, BlogView
from apps.blog.serializers import CreateCategoryModelSerializer, CategoryModelSerializer, BlogModelSerializer, \
    ListBlogModelSerializer


class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryModelSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAdminUser,)


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.order_by('-created_at')
    serializer_class = CategoryModelSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)


class RetrieveCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAdminUser,)


class DestroyCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAdminUser,)


class BlogAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title', 'description')
    permission_classes = {
        'list': (IsAuthenticated,),
        'post': (IsAdminUser,)
    }

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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # print(self.request.META.get('HTTP_USER_AGENT', ''))
        queryset = super().get_queryset()
        blog = get_object_or_404(queryset, slug=self.kwargs["slug"])
        if self.request.user.is_authenticated:
            blog_view, created = BlogView.objects.update_or_create(
                blog=blog,
                user=self.request.user,
            )
            if created:
                blog.views += 1
                blog.save()
        elif self.request.META.get('HTTP_USER_AGENT', ''):
            device_id = self.request.META.get('HTTP_USER_AGENT', '')
            blog_view, created = BlogView.objects.update_or_create(
                blog=blog,
                device_id=device_id,
            )
            if created:
                blog.views += 1
                blog.save()

        return queryset


class UpdateBlogAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    parser_classes = (MultiPartParser,)
    lookup_field = 'slug'
    permission_classes = (IsAdminUser,)


class DestroyBlogAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = 'slug'
    permission_classes = (IsAdminUser,)
