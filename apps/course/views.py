from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from .certificate_generator import certificate_generate
from ..account.models import User
from ..course.models import Category, Course, CourseView, Certificate, Content, ContentView, ContentComment
from ..course.serializers import CategorySerializer, CourseSerializer, CertificateCommentSerializer, LessonSerializer, \
    CertificateSerializer, ContentViewSerializer, ContentCommentSerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieve(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        user_id = request.GET['user_id']
        instance = self.get_object()
        serializer = CourseSerializer(instance.category_courses.all(), many=True, context={"user_id": user_id}).data
        return Response(serializer)


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.GET['user_id']
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'user_id': user_id})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer_class()(queryset, many=True, context={'user_id': user_id})
        return Response(serializer.data)


class CourseRetrieve(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        user_id = request.GET['user_id']
        instance = self.get_object()
        serializer = CourseSerializer(instance, context={'user_id': user_id}).data

        # update_view_count_task.delay(Course, instance, request.user, self.request.headers.get("device-id", None))

        device_id = self.request.META.get('HTTP_USER_AGENT', '')
        if request.user.is_authenticated:
            CourseView.objects.update_or_create(
                course=instance,
                user=request.user,
            )
        elif device_id is not None:
            CourseView.objects.update_or_create(
                course=instance,
                device_id=device_id
            )
        course_comments = instance.course_certificates.all()
        course_serializer = CertificateCommentSerializer(course_comments, many=True).data
        data = {
            'course': serializer,
            'course_comments': course_serializer,
            'course_comments_count': course_comments.count()
        }
        return Response(data)

    def get_serializer_context(self):
        context = super(CourseRetrieve, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class LessonList(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = request.GET['user_id']
        lessons = instance.course_lessons.all()
        serializer = self.get_serializer_class()(lessons, many=True, context={'user_id': user_id}).data

        return Response(serializer)


class CreateCertificate(CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def create(self, request, *args, **kwargs):
        try:
            certificate = Certificate.objects.get(course_id=request.data['course'], user_id=request.data['user'])
            serizalizer = self.get_serializer(certificate).data
            return Response(serizalizer)
        except:
            try:
                course = Course.objects.get(id=request.data['course'])
                user = User.objects.get(id=request.data['user'])
                if Content.objects.filter(lesson__course_id=course).count() == ContentView.objects.filter(
                        content__lesson__course_id=course, user_id=user, is_viewed=True).count():
                    file = certificate_generate(user, course)
                    certificate = Certificate.objects.create(course=course, user=user, file=file,
                                                             rate=request.data['rate'],
                                                             comment=request.data['comment'])
                    serizalizer = self.get_serializer(certificate).data
                    return Response(serizalizer)
                return Response({'Error': "Kurslar to'liq ko'rilmagan!"})
            except Exception as e:
                return Response({"Error": f"{e}"})


class CertificateRetrieve(RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            user = request.GET['user']
            course = request.GET['course']
            certificate = Certificate.objects.get(user_id=user, course_id=course)
            serializer = self.get_serializer(certificate).data
            return Response(serializer)
        except Exception as e:
            return Response({'Error': f'{e}'})


class CreateContentView(CreateAPIView):
    queryset = ContentView.objects.all()
    serializer_class = ContentViewSerializer

    def create(self, request, *args, **kwargs):
        contentview, created = ContentView.objects.get_or_create(content_id=request.data['content'],
                                                                 user_id=request.data['user'], is_viewed=True)
        serializer = self.get_serializer(contentview)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateContentComment(CreateAPIView):
    queryset = ContentComment.objects.all()
    serializer_class = ContentCommentSerializer
