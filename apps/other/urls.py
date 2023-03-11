from django.urls import path
from apps.other.views import *

urlpatterns = [
    path('adv/', ListAdvertisementAPIView.as_view()),
    path('rules/', ListRulesOfUseAPIView.as_view()),
    path('cont/', ListContactAPIView.as_view()),
    path('msg/', ListMessageAPIView.as_view()),
    path('notif/', ListNotification.as_view()),
]