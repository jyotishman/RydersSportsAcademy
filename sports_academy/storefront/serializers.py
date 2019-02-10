from django.conf import settings
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from sports_academy.utils.helpers import send_mail


class ContactUsSerializer(serializers.Serializer):
	full_name = serializers.CharField(max_length=100)
	email = serializers.EmailField()
	phone_number = PhoneNumberField(required=False)
	content = serializers.CharField()

	def send_contact_mail(self, validated_data):
		subject = "Regarding contact with user"
		recipient_list = settings.CONTACT_US_RECIPIENTS
		message = "Full Name - %s\nEmail - %s\nPhone Number - %s\n%s" % (
			validated_data.get('full_name'),
			validated_data.get('email'),
			validated_data.get('phone_number', "Not provided"),
			validated_data.get('content'),
		)
		return send_mail(subject, recipient_list, message, from_email=settings.DEFAULT_FROM_EMAIL)
