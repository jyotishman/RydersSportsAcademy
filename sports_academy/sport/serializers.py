from rest_framework import serializers

from sports_academy.center.serializers import CenterSerializer
from . import models


class SportSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sport
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug',)


class SportDetailSerializer(serializers.ModelSerializer):
	centers = serializers.SerializerMethodField(source='get_centers')

	class Meta:
		model = models.Sport
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug', 'centers',)

	def get_centers(self, sport):
		return CenterSerializer(sport.center_set.all(), many=True).data
