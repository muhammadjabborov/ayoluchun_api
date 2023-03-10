from rest_framework.serializers import ModelSerializer

from ..course.models import Category, Course, CourseView, Lesson, Content, ContentComment, Certificate


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = (
        'id', 'category', 'author', 'title', 'type', 'rate', 'photo', 'video', 'description', 'price', 'discount')


class CourseViewSerializer(ModelSerializer):
    class Meta:
        model = CourseView
        fields = ('id', 'course', 'user', 'device_id')


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'description')


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'lesson', 'title', 'video')


class ContentCommentSerializer(ModelSerializer):
    class Meta:
        model = ContentComment
        fields = ('id', 'content', 'user', 'comment', 'parent')


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'course', 'user', 'file', 'rate', 'comment')
