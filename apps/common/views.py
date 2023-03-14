from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.common.models import Country, Region
from apps.common.serializers import CountrySerializer, RegionSerializer


class CreateCountryAPIVIew(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdminUser,)


class ListCountryAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)


class RetrieveCountryAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


class UpdateCountryAPIView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


class DeleteCountryAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


class CreateRegionAPIVIew(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAdminUser,)


class ListRegionAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)


class RetrieveRegionAPIView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


class UpdateRegionAPIView(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


class DeleteRegionAPIView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
