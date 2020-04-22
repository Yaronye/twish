from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
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
        #hash = make_password(password.data['password'])
        if password.data['password'] == object.password:                    #request.POST['password'] == object.password, same result
            serializer = FetchSecretSerializer(instance=object)
            object.maxviews -= 1
            object.save()
            if object.maxviews <= 1:
                object.delete()
            return Response(serializer.data)
        else:
            #print(str(hash))
            return Response(b"WRONG PASSWORD")
