from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework import permissions
from .models import Secret
from .serializers import SecretSerializer, FetchSecretSerializer, PasswordSerializer


class SecretViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    lookup_field = 'uuid'
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer         #used for all methods, used if other is not specified

    @action(methods=['post'], detail=True)
    def fetch(self, request, uuid):
        try:
            object = self.queryset.get(uuid=uuid)
        except Secret.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        password = PasswordSerializer(data=request.POST)         #serializer used to check indata formatting and validation
        password.is_valid(raise_exception=True)
        if password.data['password'] == object.password:                    #request.POST['password'] == object.password, same result
            serializer = FetchSecretSerializer(instance=object)
            object.maxviews -= 1
            object.save()
            if object.maxviews <= 0:
                object.delete()
            return Response(serializer.data)
        else:
            return Response(b"WRONG PASSWORD")
