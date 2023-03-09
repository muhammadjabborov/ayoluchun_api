from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser, MultiPartParser
# from .models import *
from .serializers import *


# Create your views here.

class AdvertisementAPIView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    parser_classes = (MultiPartParser,)


class RulesOfUseAPIView(ListAPIView):
    queryset = RulesOfUse.objects.all()
    serializer_class = RulesOfUseSerializer


class ContactAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MessageAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class Notification(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    parser_classes = (MultiPartParser,)
