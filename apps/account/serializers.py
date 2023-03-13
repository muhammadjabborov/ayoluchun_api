from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, DateTimeField, ChoiceField
from rest_framework.serializers import ModelSerializer, Serializer
from ..account.models import User, JobPosition, Author


class RegistrationSerializer(Serializer):
    GENDER_TYPE = [
        ('MALE', 'Erkak'),
        ('FEMALE', 'Ayol')
    ]
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    birthday = DateTimeField()
    gender = ChoiceField(choices=GENDER_TYPE)
    phone = PhoneNumberField()
    password = CharField(max_length=255)
    confirm_password = CharField(max_length=255, write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError({"message": "This username is already exists"})
        if User.objects.filter(phone=data['phone']).exists():
            raise ValidationError({"message": "This phone_number is already exists"})
        if data['password'] != data['confirm_password']:
            raise ValidationError({"message": "Password fields didn't match"})

        return data

    @atomic
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'phone', 'password')


class UserDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'phone', 'username', 'birthday', 'gender')


class UserSerializerForComment(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'photo',)


class JobPositionSerializer(ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ('id', 'name')


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id', 'user', 'photo', 'region', 'address', 'post_code', 'instagram', 'imkon', 'linkedin', 'job',
            'position',
            'bio')
