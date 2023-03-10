from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser
# from .models import *
from .serializers import *


# Create your views here.

class ListAdvertisementAPIView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    parser_classes = (MultiPartParser,)


class ListRulesOfUseAPIView(ListAPIView):
    queryset = RulesOfUse.objects.all()
    serializer_class = RulesOfUseSerializer


class ListContactAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ListMessageAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ListNotification(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    parser_classes = (MultiPartParser,)
