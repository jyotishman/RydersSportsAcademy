from rest_framework import permissions
from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.GallerySerializer
	queryset = models.Gallery.objects.filter(active=True)
