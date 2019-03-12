from rest_framework import serializers

from . import models


class ReviewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Reviews
		fields = ('id', 'name', 'image', 'content', 'active', 'created', 'modified', 'slug',)