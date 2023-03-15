from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, DateTimeField, ChoiceField, EmailField, IntegerField, DateField
from rest_framework.serializers import ModelSerializer, Serializer
from ..account.models import User, JobPosition, Author
from ..blog.serializers import BlogModelSerializer


class RegistrationSerializer(Serializer):
    GENDER_TYPE = [
        ('MALE', 'Erkak'),
        ('FEMALE', 'Ayol')
    ]
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    email = EmailField()
    birthday = DateField()
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
        fields = (
            'id', 'photo', 'username', 'email',
            'first_name', 'last_name', 'phone',
            'username', 'birthday', 'gender'
        )


class UserSerializerForComment(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'photo',)


class JobPositionSerializer(ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ('id', 'name')


class CreateAuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id', 'user', 'photo', 'region', 'address', 'post_code', 'instagram', 'imkon', 'linkedin', 'job',
            'position',
            'bio'
        )


class ListAuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id', 'user', 'photo', 'region', 'address', 'post_code', 'instagram', 'imkon', 'linkedin', 'job',
            'position',
            'bio', 'blogs'
        )


class UpdateUserModelSerializer(ModelSerializer):
    GENDER_TYPE = [
        ('MALE', 'Erkak'),
        ('FEMALE', 'Ayol')
    ]
    first_name = CharField(max_length=255, required=False)
    last_name = CharField(max_length=255, required=False)
    username = CharField(max_length=255, required=False)
    birthday = DateField(required=False)
    gender = ChoiceField(choices=GENDER_TYPE, required=False)
    phone = PhoneNumberField(required=False)
    address = CharField(required=False)
    instagram = CharField(required=False)
    linkedin = CharField(required=False)
    imkon_uz = CharField(required=False)
    job = CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name',
            'username', 'gender', 'birthday',
            'email', 'country', 'region',
            'post_code', 'address', 'phone',
            'instagram', 'imkon_uz', 'linkedin',
            'job', 'position', 'bio', 'photo'
        )
