from rest_framework import serializers
from sports_academy.sport.fields import SportBaseField

from . import models


class CenterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Center
		fields = ('id', 'academy_name', 'image', 'description', 'address', 'city', 'state', 'country', 'mobile',
		          'email', 'zipcode', 'morning_opening_timing', 'morning_closing_timing', 'evening_opening_timing',
		          'evening_closing_timing', 'created', 'modified', 'slug',)


class CenterDetailSerializer(serializers.ModelSerializer):
	sports = SportBaseField(read_only=True, many=True)

	class Meta:
		model = models.Center
		fields = ('id', 'academy_name', 'image', 'description', 'address', 'city', 'state', 'country', 'mobile',
		          'email', 'zipcode', 'morning_opening_timing', 'morning_closing_timing', 'evening_opening_timing',
		          'evening_closing_timing', 'created', 'modified', 'slug', 'sports',)
