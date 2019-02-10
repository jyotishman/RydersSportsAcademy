from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from slugify import slugify
from autoslug import AutoSlugField


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

	def __str__(self):
		return self.academy_name
