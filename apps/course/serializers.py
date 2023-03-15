from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.account.serializers import UserSerializerForComment
from apps.common.models import PaymentStatusType
from apps.course.models import Category, Course, CourseView, Lesson, Content, ContentComment, Certificate, ContentView


class CategorySerializer(ModelSerializer):
    course_count = SerializerMethodField('course_count_func')

    def course_count_func(self, obj):
        return obj.category_courses.all().count()

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'name_ru', 'course_count')


class CourseSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = SerializerMethodField()
    is_paid = SerializerMethodField()

    def get_author(self, obj):
        return f"{obj.author.user.first_name} {obj.author.user.first_name}"

    def get_category(self, obj):
        return obj.category.name

    def get_is_paid(self, course):
        return course.course_payments.filter(payment_status_type=PaymentStatusType.SUCCESS,
                                             user_id=self.context['user_id']).exists()

    class Meta:
        model = Course
        fields = (
            'id', 'category', 'author', 'title', 'type', 'rate', 'photo', 'video', 'description', 'description_ru',
            'price', 'discount', 'slug', 'is_paid')


class CourseDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = SerializerMethodField()
    views = SerializerMethodField()
    is_paid = SerializerMethodField()
    comments = SerializerMethodField()

    def get_is_paid(self, course):
        return course.course_payments.filter(payment_status_type=PaymentStatusType.SUCCESS,
                                             user_id=self.context['user_id']).exists()

    def get_author(self, obj):
        return f"{obj.author.user.first_name} {obj.author.user.first_name}"

    def get_category(self, obj):
        return obj.category.name

    def get_views(self, obj):
        return obj.course_views.all().count()

    def get_comments(self, course):
        comments = course.course_certificates.all()
        ser = CertificateCommentSerializer(comments, many=True).data

        return ser

    class Meta:
        model = Course
        fields = (
            'id', 'category', 'author', 'title', 'type', 'rate', 'photo', 'video', 'description', 'description_ru',
            'price', 'discount', 'slug', 'views', 'is_paid', 'comments')


class CourseViewSerializer(ModelSerializer):
    class Meta:
        model = CourseView
        fields = ('id', 'course', 'user', 'device_id')


class LessonSerializer(ModelSerializer):
    videos = SerializerMethodField()
    is_viewed = SerializerMethodField()

    def get_videos(self, obj):
        serializer = ContentSerializer(obj.lesson_contents.all(), many=True).data
        return serializer

    def get_is_viewed(self, lesson):
        if ContentView.objects.filter(content__lesson=lesson, is_viewed=True,
                                      user_id=self.context['user_id']).count() == 0:
            return False
        return lesson.lesson_contents.all().count() == ContentView.objects.filter(content__lesson=lesson,
                                                                                  user_id=self.context['user_id'],
                                                                                  is_viewed=True).count()

    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'description', 'title_ru', 'description_ru', 'videos', 'is_viewed')


class ContentSerializer(ModelSerializer):
    comments = SerializerMethodField()

    def get_comments(self, content):
        serializer = ContentCommentSerializer(content.content_comments.all(), many=True).data
        return serializer

    class Meta:
        model = Content
        fields = ('id', 'lesson', 'title', 'video', 'comments')


class ContentCommentSerializer(ModelSerializer):
    user = UserSerializerForComment(read_only=True)
    replies = SerializerMethodField()

    def get_replies(self, obj):
        if obj.replies.count() == 0:
            return None
        serializer = self.__class__(obj.replies.all(), many=True)
        return serializer.data

    class Meta:
        model = ContentComment
        fields = ('id', 'user', 'comment', 'replies')


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'course', 'user', 'file', 'rate', 'comment')


class CertificateCommentSerializer(ModelSerializer):
    user = UserSerializerForComment(read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'user', 'comment', 'rate')


class ContentViewSerializer(ModelSerializer):
    class Meta:
        model = ContentView
        fields = ('id', 'user', 'content', 'is_viewed')
