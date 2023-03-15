from rest_framework.fields import IntegerField, CharField
from rest_framework.serializers import ModelSerializer

from apps.blog.models import Blog, Category


class CreateCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug', 'created_at', 'updated_at')


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'slug', 'icon'
        )


class ListBlogModelSerializer(ModelSerializer):
    views = IntegerField(read_only=True)

    # TODO
    # shuni author model serializer ni yozish kerak
    # author = AuthorModelSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id', 'title', 'slug', 'author', 'photo',
            'created_at', 'get_thumbnails', 'category', 'views'
        )


class RetrieveBlogModelSerializer(ModelSerializer):

    views = IntegerField(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id', 'title', 'author', 'category', 'views',
            'description', 'photo', 'get_thumbnails'
        )


class BlogModelSerializer(ModelSerializer):
    views = IntegerField(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id',  'author', 'category', 'views',
            'photo', 'description'
        )
