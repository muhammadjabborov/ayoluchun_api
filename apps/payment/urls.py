from django.urls import path

from apps.payment.views import CreatePaymentAPIView, ListPaymentAPIView

urlpatterns = [
    path('payment/create/', CreatePaymentAPIView.as_view(), name='payment_create'),
    path('payment/list/', ListPaymentAPIView.as_view(), name='payment_list')
]
