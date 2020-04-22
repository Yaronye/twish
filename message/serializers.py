from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Secret

class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'password', 'maxviews', 'uuid']

    def create(self, validated_data):
        secret = Secret(
            content=validated_data['content'],
            password=make_password(validated_data['password']),
            maxviews=validated_data['maxviews'],
        )
        secret.save()
        return secret

class FetchSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'maxviews']

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['password']
