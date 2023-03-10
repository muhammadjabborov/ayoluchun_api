from rest_framework.serializers import ModelSerializer
from ..account.models import User, JobPosition, Author


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'birthday', 'gender')


class JobPositionSerializer(ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ('id', 'name')


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'user', 'photo', 'region', 'address', 'post_code', 'instagram', 'imkon', 'linkedin', 'job', 'position', 'bio')
