from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.payment.models import Payment
from apps.payment.serializers import CreatePaymentModelSerializer, ListPaymentModelSerializer


class CreatePaymentAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = CreatePaymentModelSerializer
    permission_classes = (IsAuthenticated,)


class ListPaymentAPIView(ListAPIView):
    queryset = Payment.objects.order_by('-created_at')
    serializer_class = ListPaymentModelSerializer
    permission_classes = (IsAdminUser,)
