from rest_framework import serializers

from . import models


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Team
		fields = ('id', 'name', 'image', 'designation', 'about', 'active', 'sports', 'centers', 'twitter_url',
		          'facebook_url', 'instagram_url', 'google_plus_url', 'linkedin_url', 'created', 'modified', 'slug',)
