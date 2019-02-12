from rest_framework import serializers
from sports_academy.center.fields import CenterBaseField
from sports_academy.sport.fields import SportBaseField

from . import models


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Team
		fields = ('id', 'name', 'image', 'designation', 'about', 'active', 'twitter_url', 'facebook_url',
		          'instagram_url', 'google_plus_url', 'linkedin_url', 'created', 'modified', 'slug',)


class TeamDetailSerializer(serializers.ModelSerializer):
	sports = SportBaseField(read_only=True, many=True)
	centers = CenterBaseField(read_only=True, many=True)

	class Meta:
		model = models.Team
		fields = ('id', 'name', 'image', 'designation', 'about', 'active', 'sports', 'centers', 'twitter_url',
		          'facebook_url', 'instagram_url', 'google_plus_url', 'linkedin_url', 'created', 'modified', 'slug',)
