from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Secret

class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'password', 'maxviews', 'uuid']

class FetchSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'maxviews']

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['password']
