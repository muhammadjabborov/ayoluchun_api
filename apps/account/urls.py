from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.account.views import RegisterAPIView, UserDataAPIView, UpdateUserAPIView, ActivateUserAPIView, \
    SendActivationAPIView

urlpatterns = [
    path('account/login/', TokenObtainPairView.as_view(), name='login'),
    path('account/login/refresh/', TokenRefreshView.as_view(), name='login-refresh'),
    path('account/register/', RegisterAPIView.as_view(), name='register'),
    path('account/info/', UserDataAPIView.as_view(), name='info'),
    path('account/update/', UpdateUserAPIView.as_view(), name='user_update'),
    path('account/activate/<str:uidb64>/<str:token>', ActivateUserAPIView.as_view(), name='activate_user'),
    path('account/send/link/', SendActivationAPIView.as_view(), name='send_link')
]
