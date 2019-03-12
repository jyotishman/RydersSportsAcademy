from rest_framework import serializers

from . import models


class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.News
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug',)