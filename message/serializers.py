from rest_framework import serializers
from .models import Secret


# used when creating a secret
class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'password', 'maxviews', 'uuid']


# used when showing a secret
class FetchSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['content', 'maxviews']


# used when checking if the password is correct
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['password']
