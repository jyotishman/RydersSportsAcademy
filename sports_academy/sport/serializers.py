from rest_framework import serializers

from . import models


class SportSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sport
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug',)
