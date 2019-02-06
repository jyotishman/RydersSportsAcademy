from rest_framework import permissions
from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.TeamSerializer
	queryset = models.Team.objects.filter(active=True)
