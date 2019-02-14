from rest_framework import serializers

from . import models


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Company
		fields = ('id', 'name', 'twitter_url', 'facebook_url', 'instagram_url', 'google_plus_url', 'linkedin_url', 'address', 'city', 'state', 'country', 'zipcode', 'created', 'modified')