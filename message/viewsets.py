from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from .models import Secret
from .serializers import SecretSerializer, FetchSecretSerializer, PasswordSerializer


class SecretViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    lookup_field = 'uuid'                       # use uuid to look up the correct database object instead of using pk
    queryset = Secret.objects.all()             # access the objects from the database
    serializer_class = SecretSerializer         # used if other is not specified

    @action(methods=['post'], detail=True)
    def send(self, request, uuid):
        try:
            object = self.queryset.get(uuid=uuid)
        except Secret.DoesNotExist:
            return Response({"message": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)
        password = PasswordSerializer(data=request.POST)     # serializer used to check indata formatting and validation
        password.is_valid(raise_exception=True)
        if password.data['password'] == object.password:
            serializer = FetchSecretSerializer(instance=object)
            object.maxviews -= 1
            object.save()
            if object.maxviews <= 1:
                object.delete()
            return Response(serializer.data)
        else:
            return Response({"message": "WRONG PASSWORD"}, status=status.HTTP_403_FORBIDDEN)
