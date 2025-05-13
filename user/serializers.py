# from rest_framework.serializers import ModelSerializer, Serializer
# from user.models import User
# from rest_framework import serializers
#
#
# class RegisterSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#
#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=255)

from rest_framework.serializers import ModelSerializer, Serializer
from user.models import User
from rest_framework import serializers


# serializers.py
from rest_framework import serializers
from .models import User, VerificationCode
from .utils import generate_verification_code, send_verification_email

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            verified=False
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create code and send email
        code = generate_verification_code()
        VerificationCode.objects.update_or_create(user=user, defaults={'code': code})
        send_verification_email(user.email, code)

        return user

class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # `username` o‘rniga `email`
    password = serializers.CharField(write_only=True)


