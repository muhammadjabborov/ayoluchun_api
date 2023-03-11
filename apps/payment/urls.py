from django.urls import path
from .views import PaymentAPIView
urlpatterns = [
    path('', PaymentAPIView.as_view())
]