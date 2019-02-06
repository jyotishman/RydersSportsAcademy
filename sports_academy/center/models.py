from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.


class Center(models.Model):
	academy_name = models.CharField(max_length=200)
	image = models.ImageField(null=True)
	description = models.TextField(blank=True)

	address = models.TextField(blank=True)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	mobile = PhoneNumberField()
	email = models.EmailField(max_length=255, blank=True)
	zipcode = models.CharField(max_length=10, blank=True)

	morning_opening_timing = models.TimeField()
	morning_closing_timing = models.TimeField()

	evening_opening_timing = models.TimeField()
	evening_closing_timing = models.TimeField()

	sports = models.ManyToManyField('sport.Sport')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		self.academy_name