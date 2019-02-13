from autoslug import AutoSlugField
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Center(models.Model):
	academy_name = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True)
	description = models.TextField(blank=True)

	address = models.TextField(blank=True)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=10)

	active = models.BooleanField(default=True)

	mobile = PhoneNumberField(blank=True)
	email = models.EmailField(max_length=255, blank=True)

	morning_opening_timing = models.TimeField(null=True, blank=True)
	morning_closing_timing = models.TimeField(null=True, blank=True)

	evening_opening_timing = models.TimeField(null=True, blank=True)
	evening_closing_timing = models.TimeField(null=True, blank=True)

	sports = models.ManyToManyField('sport.Sport')

	slug = AutoSlugField(populate_from='academy_name', null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def clean(self):
		if self.morning_opening_timing > self.morning_closing_timing or \
						self.evening_opening_timing > self.evening_closing_timing:
			raise ValidationError("Opening timing should be greater than closing timing")

	def __str__(self):
		return self.academy_name
