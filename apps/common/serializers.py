from rest_framework.serializers import ModelSerializer

from ..common.models import Country, Region


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'slug')


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'slug')

