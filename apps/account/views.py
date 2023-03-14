from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.account.models import User, Author
from apps.account.serializers import RegistrationSerializer, UserDataSerializer, CreateAuthorModelSerializer, \
    ListAuthorModelSerializer, UpdateUserModelSerializer


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
