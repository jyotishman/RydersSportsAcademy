from rest_framework import serializers

from . import models


class CenterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Center
		fields = ('id', 'academy_name', 'image', 'description', 'address', 'city', 'state', 'country', 'mobile',
		          'email', 'zipcode', 'morning_opening_timing', 'morning_closing_timing', 'evening_opening_timing',
		          'evening_closing_timing', 'sports', 'created', 'modified', 'slug',)
