from rest_framework import permissions
from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.


class CenterViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.CenterSerializer
	queryset = models.Center.objects.all()
