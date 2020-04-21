from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import permissions
from .models import Secret
from .serializers import SecretSerializer, FetchSecretSerializer, PasswordSerializer


class SecretViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer         #used for all methods, used if other is not specified

    @action(methods=['post'], detail=True)
    def fetch(self, request, pk):
        object = self.queryset.get(pk=pk)
        password = PasswordSerializer(data=request.POST)         #serializer used to check indata formatting and validation
        password.is_valid(raise_exception=True)
        if password.data['password'] == object.password:                    #request.POST['password'] == object.password, same result
            serializer = FetchSecretSerializer(instance=object)
            return Response(serializer.data)
        else:
            return Response(b"WRONG PASSWORD")

    #@action(methods=['get'], detail=True)
    #def create(self):
    #    return Response(b"content = message, password = secret to gain aces")