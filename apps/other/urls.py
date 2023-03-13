from django.urls import path
from apps.other.views import *

urlpatterns = [
    path('main/advertisement/', ListAdvertisementAPIView.as_view()),
    path('main/rules/', ListRulesOfUseAPIView.as_view()),
    path('main/contact/', CreateContactAPIView.as_view()),
    path('main/message/', MessageAPIView.as_view()),
    path('main/notification/', ListNotification.as_view()),
]
