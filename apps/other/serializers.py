from rest_framework import serializers
from .models import *


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('id', 'title',
                  'photo', 'description',
                  'link', 'is_active')


class RulesOfUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RulesOfUse
        fields = ('id', 'title', 'description')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'title', 'phone',
                  'email', 'address', 'map')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'name', 'phone', 'email', 'msg')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'photo', 'context')
