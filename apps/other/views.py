from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

# from .models import *
from .serializers import *


class ListAdvertisementAPIView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)


class ListRulesOfUseAPIView(ListAPIView):
    queryset = RulesOfUse.objects.all()
    serializer_class = RulesOfUseSerializer
    permission_classes = (IsAuthenticated,)


class MessageAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class ListNotification(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)


class CreateContactAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
