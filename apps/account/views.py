from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.account.models import User, Author
from apps.account.serializers import RegistrationSerializer, UserDataSerializer, CreateAuthorModelSerializer, \
    ListAuthorModelSerializer


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


class CreateAuthorAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = CreateAuthorModelSerializer
    permission_classes = (IsAuthenticated,)


class ListAuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = ListAuthorModelSerializer
    permission_classes = (IsAuthenticated,)

# THIS VIEWS URLS IN BLOG APP
