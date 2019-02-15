from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers


# Create your views here.


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = serializers.CompanySerializer
	queryset = models.Company.objects.filter()

	def list(self, request, *args, **kwargs):
		company = self.queryset.first()
		if company:
			serializer = self.get_serializer(company)
			return Response(serializer.data)
		else:
			return Response(status=404)
