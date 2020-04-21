from django.urls import include, path
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('message', viewsets.SecretViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]
