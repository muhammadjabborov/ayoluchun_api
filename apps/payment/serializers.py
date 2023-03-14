from rest_framework.serializers import ModelSerializer

from apps.course.serializers import CourseSerializer
from apps.payment.models import Payment


class CreatePaymentModelSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user', 'sum', 'course', 'payment_type', 'payment_status_type')


class ListPaymentModelSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'user', 'sum', 'course', 'payment_type', 'payment_status_type')
