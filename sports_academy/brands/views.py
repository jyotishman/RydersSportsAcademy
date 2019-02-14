from rest_framework import permissions
from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.BrandSerializer
	queryset = models.Brands.objects.filter(active=True)
