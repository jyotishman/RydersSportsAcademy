from django.conf import settings
from django.db import models
from  autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

from sports_academy.utils.helpers import send_mail


# Create your models here.


class ContactUs(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = PhoneNumberField(blank=True)
	sport = models.CharField(max_length=100, blank=True)
	content = models.TextField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Enquires"

	def __str__(self):
		return "%s | Email - %s | Sport - %s" % (self.full_name, self.email, self.sport)

	def send_contact_mail(self):
		subject = "Regarding contact with user"
		recipient_list = settings.CONTACT_US_RECIPIENTS
		message = "Full Name - %s\nEmail - %s\nPhone Number - %s\nSport - %s\n%s" % (
			self.full_name,
			self.email,
			self.phone_number or "N.A.",
			self.sport or "N.A.",
			self.content
		)
		return send_mail(subject, recipient_list, message)


class Notification(models.Model):
	title = models.CharField(max_length=100)
	short_description = models.CharField(max_length=100)
	description = models.TextField()
	active = models.BooleanField(default=False)

	slug = AutoSlugField(populate_from='title')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
