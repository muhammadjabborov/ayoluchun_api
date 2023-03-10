from rest_framework.generics import ListCreateAPIView
from .models import Payment
from .serializers import PaymentSerializer
# Create your views here.

class PaymentAPIView(ListCreateAPIView):
    queryset = Payment
    serializer_class = PaymentSerializer