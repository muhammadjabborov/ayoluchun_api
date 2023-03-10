from rest_framework import serializers
from .models import *


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user', 'sum', 'course',
                  'payment_type', 'payment_status_type')
