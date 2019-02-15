from rest_framework import serializers

from . import models


class ContactUsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ContactUs
		fields = ('id', 'full_name', 'email', 'phone_number', 'sport', 'content', 'created', 'modified')

	def create(self, validated_data):
		instance = super(ContactUsSerializer, self).create(validated_data)
		return instance.send_contact_mail()
