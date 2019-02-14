from rest_framework import serializers

from . import models


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Brands
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug',)