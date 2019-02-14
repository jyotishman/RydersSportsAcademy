from rest_framework import permissions
from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.CompanySerializer
	queryset = models.Company.objects.filter(active=True)
