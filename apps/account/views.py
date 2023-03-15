from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse
from apps.account.models import User, Author
from apps.account.serializers import RegistrationSerializer, UserDataSerializer, CreateAuthorModelSerializer, \
    ListAuthorModelSerializer, UpdateUserModelSerializer
from apps.account.utils import account_activation_token
from django.utils.encoding import force_str, force_bytes


class RegisterAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserDataAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status.HTTP_200_OK)


# START
class CreateAuthorAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = CreateAuthorModelSerializer
    permission_classes = (IsAuthenticated,)


class ListAuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = ListAuthorModelSerializer
    permission_classes = (IsAuthenticated,)


# END
# THIS VIEWS URLS IN BLOG APP

class UpdateUserAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserModelSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SendActivationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        protocol = 'https' if request.is_secure() else 'http'
        domain = get_current_site(request).domain
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        activation_link = reverse('activate_user', kwargs={'uidb64': uidb64, 'token': token})
        activation_url = f'{protocol}://{domain}{activation_link}'
        subject = f'Activate your account on Ayol Uchun'
        message = f'Hi {user.username},\n\nPlease click the link below to activate your account on Ayol Uchun:\n\n{activation_url}'
        send_mail(
            subject=subject,
            message=message,
            from_email='no-reply@ayoluchun.com',
            recipient_list=[user.email],
            fail_silently=False
        )
        return Response({'message': f'Activation email sent to {user.email}. Check your inbox.'}, status.HTTP_200_OK)


class ActivateUserAPIView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_gmail_active = True
            user.save()
            return Response({'message': 'User is activated'})
        return Response({'message': 'invalid link'}, status.HTTP_404_NOT_FOUND)
